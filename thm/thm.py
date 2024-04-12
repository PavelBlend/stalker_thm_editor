import external
from . import fmt
from . import read
from . import types


chunk_functions = {
    fmt.Chunks.VERSION:                     read.read_version,
    fmt.Chunks.DATA:                        read.read_data,
    fmt.Chunks.TEXTURE_PARAM:               read.read_texture_param,
    fmt.Chunks.TEXTURE_TYPE:                read.read_texture_type,
    fmt.Chunks.DETAIL_EXT:                  read.read_detail_ext,
    fmt.Chunks.TYPE:                        read.read_type,
    fmt.Chunks.MATERIAL_OR_OBJECTPARAMS:    read.read_mat_or_obj_params,
    fmt.Chunks.BUMP:                        read.read_bump,
    fmt.Chunks.EXT_NORMALMAP:               read.read_ext_normalmap,
    fmt.Chunks.FADE_DELAY:                  read.read_fade_delay,
    fmt.Chunks.SOUNDPARAM:                  read.read_sound_param,
    fmt.Chunks.SOUNDPARAM2:                 read.read_sound_param_2,
    fmt.Chunks.SOUND_AI_DIST:               read.read_sound_ai_dist,
    fmt.Chunks.GROUPPARAM:                  read.read_group_param
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
    chunks = {}
    chunked_reader = external.xray_io.ChunkedReader(thm_data)

    for chunk_id, chunk_data in chunked_reader:
        chunks[chunk_id] = chunk_data

    return chunks


def _read_type(chunks):
    type_chunk = chunks.pop(fmt.Chunks.TYPE)
    thm_type = read.read_type(type_chunk)

    return thm_type


def _read_version(chunks):
    version_chunk = chunks.pop(fmt.Chunks.VERSION)
    version = read.read_version(version_chunk)

    return version


def _create_thm_object(thm_type, version):
    thm_obj = thm_classes[(version, thm_type)]()
    thm_obj.file_type = thm_type
    thm_obj.version = version

    return thm_obj


def _read_thm_params(chunks, thm_obj):
    for chunk_id, chunk_data in chunks.items():

        chunk_function = chunk_functions.get(chunk_id)

        if chunk_function:
            chunk_function(chunk_data, thm_obj)

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
