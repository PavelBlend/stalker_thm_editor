import external
from . import fmt
from . import read
from . import tex
from . import obj
from . import snd
from . import group
from . import types


chunk_functions = {
    fmt.ThmChunks.DATA:                     read.read_data,

    fmt.ThmTextureChunks.TEXTURE_PARAM:     tex.read_texture_param,
    fmt.ThmTextureChunks.TEXTURE_TYPE:      tex.read_texture_type,
    fmt.ThmTextureChunks.DETAIL_EXT:        tex.read_detail_ext,
    fmt.ThmTextureChunks.BUMP:              tex.read_bump,
    fmt.ThmTextureChunks.EXT_NORMALMAP:     tex.read_ext_normalmap,
    fmt.ThmTextureChunks.FADE_DELAY:        tex.read_fade_delay,

    fmt.ThmSoundChunks.SOUND_PARAM:         snd.read_sound_param,
    fmt.ThmSoundChunks.SOUND_BASE_VOLUME:   snd.read_sound_base_volume,
    fmt.ThmSoundChunks.SOUND_AI_DIST:       snd.read_sound_ai_dist,

    fmt.ThmGroupChunks.GROUP_PARAM:         group.read_group_param
}

thm_classes = {
    (fmt.Version.GROUP,     fmt.Type.OBJECT):   types.ThumbnailGroup,
    (fmt.Version.OBJECT,    fmt.Type.OBJECT):   types.ThumbnailObject,
    (fmt.Version.TEXTURE,   fmt.Type.TEXTURE):  types.ThumbnailTexture,
    (fmt.Version.SOUND,     fmt.Type.SOUND):    types.ThumbnailSound
}


def _read_file(thm_file_path):
    with open(thm_file_path, 'rb') as thm_file:
        thm_data = thm_file.read()

    return thm_data


def _get_chunks(thm_data):
    chunked_reader = external.xray_io.ChunkedReader(thm_data)
    return {chunk_id: chunk_data for chunk_id, chunk_data in chunked_reader}


def _read_type(chunks):
    type_chunk = chunks.pop(fmt.ThmChunks.TYPE)
    packed_reader = external.xray_io.PackedReader(type_chunk)
    thm_type = read.read_type(packed_reader)

    if thm_type not in fmt.Type.SUPPORTED:
        raise BaseException('unsupported *.thm type: {}'.format(thm_type))

    return thm_type


def _read_version(chunks):
    version_chunk = chunks.pop(fmt.ThmChunks.VERSION)
    packed_reader = external.xray_io.PackedReader(version_chunk)
    version = read.read_version(packed_reader)

    if version not in fmt.Version.SUPPORTED:
        raise BaseException('unsupported *.thm version: {}'.format(version))

    return version


def _create_thm_object(thm_type, version):
    thm_obj = thm_classes[(version, thm_type)]()
    thm_obj.file_type = thm_type
    thm_obj.version = version

    return thm_obj


def _read_thm_params(chunks, thm_obj):

    # OBJECT_PARAM and MATERIAL chunks have the same ID.
    # We need to add the necessary reading function.
    if thm_obj.file_type == fmt.Type.OBJECT:
        chunk_functions.update({fmt.ThmObjectChunks.OBJECT_PARAM: obj.read_obj_params})
    else:
        chunk_functions.update({fmt.ThmTextureChunks.MATERIAL: tex.read_mat})

    for chunk_id, chunk_data in chunks.items():

        packed_reader = external.xray_io.PackedReader(chunk_data)
        chunk_function = chunk_functions.get(chunk_id)

        if chunk_function:
            chunk_function(packed_reader, thm_obj)

        else:
            chink_size = len(chunk_data)
            print('Unknown *.thm chunk:')
            print('    ID: 0x{:x}, Size: {}\n'.format(chunk_id, chink_size))


def read_thm(thm_file_path):
    thm_data    = _read_file            (thm_file_path)
    chunks      = _get_chunks           (thm_data)
    thm_type    = _read_type            (chunks)
    version     = _read_version         (chunks)
    thm_obj     = _create_thm_object    (thm_type, version)

    _read_thm_params(chunks, thm_obj)

    return thm_obj
