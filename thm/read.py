import external
from . import fmt


def read_version(data):
    packed_reader = external.xray_io.PackedReader(data)

    version = packed_reader.getf('H')[0]

    if version not in fmt.SUPPORTED_VERSIONS:
        raise BaseException('unsupported *.thm version: {}'.format(version))

    return version


def read_data(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    if len(data) != fmt.THUMB_SIZE:
        print('length data != {}'.format(THUMB_SIZE))

    pixel_data = [
        packed_reader.getf('4B')    # red, green, blue, alpha
        for i in range(fmt.THUMB_PIXELS_COUNT)
    ]

    thm.set_data(pixel_data)


def read_type(data):
    packed_reader = external.xray_io.PackedReader(data)

    thm_type = packed_reader.getf('I')[0]

    if thm_type not in fmt.SUPPORTED_TYPES:
        raise BaseException('unsupported *.thm type: {}'.format(thm_type))

    return thm_type


def read_material_or_object_params(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    if thm.file_type == fmt.TYPE_OBJECT:
        face_count = packed_reader.getf('I')[0]
        vertex_count = packed_reader.getf('I')[0]

        thm.set_object_param(face_count, vertex_count)

    elif thm.file_type == fmt.TYPE_TEXTURE:
        material = packed_reader.getf('I')[0]
        material_weight = packed_reader.getf('f')[0]

        thm.set_material(material, material_weight)

    else:
        print('unsupported *.thm params')


def read_bump(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    bump_virtual_height = packed_reader.getf('f')[0]
    bump_mode = packed_reader.getf('I')[0]
    bump_name = packed_reader.gets()

    thm.set_bump(bump_virtual_height, bump_mode, bump_name)


def read_ext_normalmap(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    ext_normal_map_name = packed_reader.gets()

    thm.set_ext_normal_map_name(ext_normal_map_name)


def read_texture_param(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    texture_format = packed_reader.getf('I')[0]
    flags = packed_reader.getf('I')[0]
    border_color = packed_reader.getf('I')[0]
    fade_color = packed_reader.getf('I')[0]
    fade_amount = packed_reader.getf('I')[0]
    mip_filter = packed_reader.getf('I')[0]
    width = packed_reader.getf('I')[0]
    height = packed_reader.getf('I')[0]

    thm.set_texture_param(texture_format, flags, border_color, fade_color,
        fade_amount, mip_filter, width, height
    )


def read_texture_type(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    texture_type = packed_reader.getf('I')[0]

    thm.set_texture_type(texture_type)


def read_detail_ext(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    detail_name = packed_reader.gets()
    detail_scale = packed_reader.getf('f')[0]

    thm.set_detail_ext(detail_name, detail_scale)


def read_fade_delay(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    fade_delay = packed_reader.getf('B')[0]

    thm.set_fade_delay(fade_delay)


def read_sound_param(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    quality = packed_reader.getf('f')[0]
    min_dist = packed_reader.getf('f')[0]
    max_dist = packed_reader.getf('f')[0]
    game_type = packed_reader.getf('I')[0]

    thm.set_params(quality, min_dist, max_dist, game_type)


def read_sound_param_2(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    base_volume = packed_reader.getf('f')[0]

    thm.set_params_2(base_volume)


def read_sound_ai_dist(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    max_ai_dist = packed_reader.getf('f')[0]

    thm.set_ai_dist(max_ai_dist)


def read_group_param(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    objects_count = packed_reader.getf('I')[0]

    for object_index in range(objects_count):
        object_name = packed_reader.gets()

        thm.set_object_name(object_name)
