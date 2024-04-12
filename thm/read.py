import external
from . import fmt


def read_version(packed_reader):
    version = packed_reader.getf('<H')[0]

    return version


def read_data(packed_reader, thm):
    if packed_reader.size != fmt.THUMB_SIZE:
        print('length data != {}'.format(THUMB_SIZE))

    thm.data = [
        packed_reader.getf('<4B')    # red, green, blue, alpha
        for i in range(fmt.THUMB_PIXELS_COUNT)
    ]


def read_type(packed_reader):
    thm_type = packed_reader.getf('<I')[0]

    return thm_type


def read_obj_params(packed_reader, thm):
    thm.face_count      = packed_reader.getf('<I')[0]
    thm.vertex_count    = packed_reader.getf('<I')[0]


def read_mat(packed_reader, thm):
    thm.material        = packed_reader.getf('<I')[0]
    thm.material_weight = packed_reader.getf('<f')[0]


def read_bump(packed_reader, thm):
    thm.bump_virtual_height = packed_reader.getf('<f')[0]
    thm.bump_mode           = packed_reader.getf('<I')[0]
    thm.bump_name           = packed_reader.gets()


def read_ext_normalmap(packed_reader, thm):
    thm.ext_normal_map_name = packed_reader.gets()


def read_texture_param(packed_reader, thm):
    tex_fmt_id          = packed_reader.getf('<I')[0]
    thm.texture_format  = fmt.tex_fmt_names.get(tex_fmt_id, 'Unknown')
    thm.flags           = packed_reader.getf('<I')[0]
    thm.border_color    = packed_reader.getf('<I')[0]
    thm.fade_color      = packed_reader.getf('<I')[0]
    thm.fade_amount     = packed_reader.getf('<I')[0]
    thm.mip_filter      = packed_reader.getf('<I')[0]
    thm.width           = packed_reader.getf('<I')[0]
    thm.height          = packed_reader.getf('<I')[0]


def read_texture_type(packed_reader, thm):
    thm.texture_type = packed_reader.getf('<I')[0]


def read_detail_ext(packed_reader, thm):
    thm.detail_name     = packed_reader.gets()
    thm.detail_scale    = packed_reader.getf('<f')[0]


def read_fade_delay(packed_reader, thm):
    thm.fade_delay = packed_reader.getf('<B')[0]


def read_sound_param(packed_reader, thm):
    thm.quality     = packed_reader.getf('<f')[0]
    thm.min_dist    = packed_reader.getf('<f')[0]
    thm.max_dist    = packed_reader.getf('<f')[0]
    thm.game_type   = packed_reader.getf('<I')[0]


def read_sound_base_volume(packed_reader, thm):
    thm.base_volume = packed_reader.getf('<f')[0]


def read_sound_ai_dist(packed_reader, thm):
    thm.max_ai_dist = packed_reader.getf('<f')[0]


def read_group_param(packed_reader, thm):
    objects_count = packed_reader.getf('<I')[0]

    for object_index in range(objects_count):
        object_name = packed_reader.gets()

        thm.objects_names.append(object_name)
