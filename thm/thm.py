
from . import format_
from .external.io_scene_xray import xray_io
from . import read
from . import types


def main():
    thm_file = open('C:\\Users\\Pavel\\Desktop\\thm_editor\\thm\\act_antigas.thm', 'rb')
    thm_data = thm_file.read()
    thm_file.close()

    thm = types.Thumbnail()
    chunked_reader = xray_io.ChunkedReader(thm_data)

    for chunk_id, chunk_data in chunked_reader:

        if chunk_id == format_.Chunks.VERSION:
            read.read_version(chunk_data, thm)

        elif chunk_id == format_.Chunks.DATA:
            read.read_data(chunk_data, thm)

        elif chunk_id == format_.Chunks.TEXTURE_PARAM:
            read.read_texture_param(chunk_data, thm)

        elif chunk_id == format_.Chunks.TEXTURE_TYPE:
            read.read_texture_type(chunk_data, thm)

        elif chunk_id == format_.Chunks.DETAIL_EXT:
            read.read_detail_ext(chunk_data, thm)

        elif chunk_id == format_.Chunks.TYPE:
            read.read_type(chunk_data, thm)

        elif chunk_id == format_.Chunks.MATERIAL:
            read.read_material(chunk_data, thm)

        elif chunk_id == format_.Chunks.BUMP:
            read.read_bump(chunk_data, thm)

        elif chunk_id == format_.Chunks.EXT_NORMALMAP:
            read.read_ext_normalmap(chunk_data, thm)

        elif chunk_id == format_.Chunks.FADE_DELAY:
            read.read_fade_delay(chunk_data, thm)

        elif chunk_id == format_.Chunks.SOUNDPARAM:
            read.read_sound_param(chunk_data, thm)

        elif chunk_id == format_.Chunks.SOUNDPARAM2:
            read.read_sound_param_2(chunk_data, thm)

        elif chunk_id == format_.Chunks.SOUND_AI_DIST:
            read.read_sound_ai_dist(chunk_data, thm)

        elif chunk_id == format_.Chunks.GROUPPARAM:
            read.read_group_param(chunk_data, thm)

        else:
            print('unknown *.thm chunk: 0x{:x}'.format(chunk_id), len(chunk_data))
