
from external import xray_io
from . import format_


def read_version(data, thm):
    packed_reader = xray_io.PackedReader(data)

    thm.version = packed_reader.getf('H')[0]

    if thm.version not in format_.SUPPORTED_VERSIONS:
        raise BaseException('unsupported *.thm version: {}'.format(thm.version))


def read_data(data, thm):
    packed_reader = xray_io.PackedReader(data)

    if len(data) != format_.THUMB_SIZE * 4:
        print('length data != 65 536')

    for data_index in range(format_.THUMB_SIZE):
        red, green, blue, alpha = packed_reader.getf('4B')
        thm.data.extend((red, green, blue, alpha))


def read_type(data, thm):
    packed_reader = xray_io.PackedReader(data)

    thm.type_ = packed_reader.getf('I')[0]

    if thm.type_ not in format_.SUPPORTED_TYPES:
        raise BaseException('unsupported *.thm type: {}'.format(thm.type_))


def read_material(data, thm):
    packed_reader = xray_io.PackedReader(data)

    if thm.type_ == format_.TYPE_OBJECT:
        thm.face_count = packed_reader.getf('I')[0]
        thm.vertex_count = packed_reader.getf('I')[0]

    elif thm.type_ == format_.TYPE_TEXTURE:
        material = packed_reader.getf('I')[0]
        material_weight = packed_reader.getf('f')[0]

    else:
        print('unsupported *.thm object param')


def read_bump(data, thm):
    packed_reader = xray_io.PackedReader(data)

    bump_virtual_height = packed_reader.getf('f')[0]
    bump_mode = packed_reader.getf('I')[0]
    bump_name = packed_reader.gets()


def read_ext_normalmap(data, thm):
    packed_reader = xray_io.PackedReader(data)

    ext_normal_map_name = packed_reader.gets()


def read_texture_param(data, thm):
    packed_reader = xray_io.PackedReader(data)

    texture_format = packed_reader.getf('I')[0]
    flags = packed_reader.getf('I')[0]
    border_color = packed_reader.getf('I')[0]
    fade_color = packed_reader.getf('I')[0]
    fade_amount = packed_reader.getf('I')[0]
    mip_filter = packed_reader.getf('I')[0]
    width = packed_reader.getf('I')[0]
    height = packed_reader.getf('I')[0]


def read_texture_type(data, thm):
    packed_reader = xray_io.PackedReader(data)

    texture_type = packed_reader.getf('I')[0]


def read_detail_ext(data, thm):
    packed_reader = xray_io.PackedReader(data)

    detail_name = packed_reader.gets()
    detail_scale = packed_reader.getf('f')[0]


def read_fade_delay(data, thm):
    packed_reader = xray_io.PackedReader(data)

    fade_delay = packed_reader.getf('B')[0]


def read_sound_param(data, thm):
    packed_reader = xray_io.PackedReader(data)

    quality = packed_reader.getf('f')[0]
    min_dist = packed_reader.getf('f')[0]
    max_dist = packed_reader.getf('f')[0]
    game_type = packed_reader.getf('I')[0]


def read_sound_param_2(data, thm):
    packed_reader = xray_io.PackedReader(data)

    base_volume = packed_reader.getf('f')[0]


def read_sound_ai_dist(data, thm):
    packed_reader = xray_io.PackedReader(data)

    max_ai_dist = packed_reader.getf('f')[0]


def read_group_param(data, thm):
    packed_reader = xray_io.PackedReader(data)

    objects_count = packed_reader.getf('I')[0]
    for object_index in range(objects_count):
        object_name = packed_reader.gets()
