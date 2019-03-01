
from external import xray_io
from . import format_
from . import read
from . import types


chunk_functions = {
    format_.Chunks.VERSION: read.read_version,
    format_.Chunks.DATA: read.read_data,
    format_.Chunks.TEXTURE_PARAM: read.read_texture_param,
    format_.Chunks.TEXTURE_TYPE: read.read_texture_type,
    format_.Chunks.DETAIL_EXT: read.read_detail_ext,
    format_.Chunks.TYPE: read.read_type,
    format_.Chunks.MATERIAL_OR_OBJECTPARAMS: read.read_material_or_object_params,
    format_.Chunks.BUMP: read.read_bump,
    format_.Chunks.EXT_NORMALMAP: read.read_ext_normalmap,
    format_.Chunks.FADE_DELAY: read.read_fade_delay,
    format_.Chunks.SOUNDPARAM: read.read_sound_param,
    format_.Chunks.SOUNDPARAM2: read.read_sound_param_2,
    format_.Chunks.SOUND_AI_DIST: read.read_sound_ai_dist,
    format_.Chunks.GROUPPARAM: read.read_group_param
}

thm_classes = {
    (format_.GROUP_VERSION, format_.TYPE_OBJECT): types.ThumbnailGroup,
    (format_.OBJECT_VERSION, format_.TYPE_OBJECT): types.ThumbnailObject,
    (format_.TEXTURE_VERSION, format_.TYPE_TEXTURE): types.ThumbnailTexture,
    (format_.SOUND_VERSION, format_.TYPE_SOUND): types.ThumbnailSound
}


def read_thm(thm_file_path):
    thm_file = open(thm_file_path, 'rb')
    thm_data = thm_file.read()
    thm_file.close()

    chunked_reader = xray_io.ChunkedReader(thm_data)
    chunks = {}

    for chunk_id, chunk_data in chunked_reader:
        chunks[chunk_id] = chunk_data

    type_chunk = chunks.pop(format_.Chunks.TYPE)
    type_ = read.read_type(type_chunk)

    version_chunk = chunks.pop(format_.Chunks.VERSION)
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
