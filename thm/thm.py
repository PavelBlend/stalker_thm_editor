import external
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
    (fmt.Version.GROUP, fmt.Type.OBJECT): types.ThumbnailGroup,
    (fmt.Version.OBJECT, fmt.Type.OBJECT): types.ThumbnailObject,
    (fmt.Version.TEXTURE, fmt.Type.TEXTURE): types.ThumbnailTexture,
    (fmt.Version.SOUND, fmt.Type.SOUND): types.ThumbnailSound
}


def read_thm(thm_file_path):

    # read file
    with open(thm_file_path, 'rb') as thm_file:
        thm_data = thm_file.read()

    # get chunks
    chunks = {}
    chunked_reader = external.xray_io.ChunkedReader(thm_data)
    for chunk_id, chunk_data in chunked_reader:
        chunks[chunk_id] = chunk_data

    # get *.thm type
    type_chunk = chunks.pop(fmt.Chunks.TYPE)
    thm_type = read.read_type(type_chunk)

    # get format version
    version_chunk = chunks.pop(fmt.Chunks.VERSION)
    version = read.read_version(version_chunk)

    # create thumbnail object
    thm = thm_classes[(version, thm_type)]()
    thm.file_type = thm_type
    thm.version = version

    # read params
    for chunk_id, chunk_data in chunks.items():
        chunk_function = chunk_functions.get(chunk_id)

        if chunk_function:
            chunk_function(chunk_data, thm)

        else:
            print('unknown *.thm chunk: 0x{:x} {}'.format(
                chunk_id,
                len(chunk_data)
            ))

    return thm
