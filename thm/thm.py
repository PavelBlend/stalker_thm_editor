
from external import xray_io
from . import fmt
from . import read
from . import types


chunk_functions = {
    fmt.Chunks.VERSION: read.read_version,
    fmt.Chunks.DATA: read.read_data,
    fmt.Chunks.TEXTURE_PARAM: read.read_texture_param,
    fmt.Chunks.TEXTURE_TYPE: read.read_texture_type,
    fmt.Chunks.DETAIL_EXT: read.read_detail_ext,
    fmt.Chunks.TYPE: read.read_type,
    fmt.Chunks.MATERIAL_OR_OBJECTPARAMS: read.read_material_or_object_params,
    fmt.Chunks.BUMP: read.read_bump,
    fmt.Chunks.EXT_NORMALMAP: read.read_ext_normalmap,
    fmt.Chunks.FADE_DELAY: read.read_fade_delay,
    fmt.Chunks.SOUNDPARAM: read.read_sound_param,
    fmt.Chunks.SOUNDPARAM2: read.read_sound_param_2,
    fmt.Chunks.SOUND_AI_DIST: read.read_sound_ai_dist,
    fmt.Chunks.GROUPPARAM: read.read_group_param
}

thm_classes = {
    (fmt.GROUP_VERSION, fmt.TYPE_OBJECT): types.ThumbnailGroup,
    (fmt.OBJECT_VERSION, fmt.TYPE_OBJECT): types.ThumbnailObject,
    (fmt.TEXTURE_VERSION, fmt.TYPE_TEXTURE): types.ThumbnailTexture,
    (fmt.SOUND_VERSION, fmt.TYPE_SOUND): types.ThumbnailSound
}


def read_thm(thm_file_path):
    thm_file = open(thm_file_path, 'rb')
    thm_data = thm_file.read()
    thm_file.close()

    chunked_reader = xray_io.ChunkedReader(thm_data)
    chunks = {}

    for chunk_id, chunk_data in chunked_reader:
        chunks[chunk_id] = chunk_data

    type_chunk = chunks.pop(fmt.Chunks.TYPE)
    type_ = read.read_type(type_chunk)

    version_chunk = chunks.pop(fmt.Chunks.VERSION)
    version = read.read_version(version_chunk)

    thm = thm_classes[(version, type_)]()
    thm.set_type(type_)
    thm.set_version(version)

    for chunk_id, chunk_data in chunks.items():
        chunk_function = chunk_functions.get(chunk_id)

        if chunk_function:
            chunk_function(chunk_data, thm)

        else:
            print('unknown *.thm chunk: 0x{:x}'.format(chunk_id), len(chunk_data))

    return thm
