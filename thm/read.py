import external
from . import fmt


def read_version(data):
    packed_reader = external.xray_io.PackedReader(data)

    version = packed_reader.getf('<H')[0]

    if version not in fmt.Version.SUPPORTED:
        raise BaseException('unsupported *.thm version: {}'.format(version))

    return version


def read_data(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    if len(data) != fmt.THUMB_SIZE:
        print('length data != {}'.format(THUMB_SIZE))

    thm.data = [
        packed_reader.getf('<4B')    # red, green, blue, alpha
        for i in range(fmt.THUMB_PIXELS_COUNT)
    ]


def read_type(data):
    packed_reader = external.xray_io.PackedReader(data)

    thm_type = packed_reader.getf('<I')[0]

    if thm_type not in fmt.Type.SUPPORTED:
        raise BaseException('unsupported *.thm type: {}'.format(thm_type))

    return thm_type


def read_material_or_object_params(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    if thm.file_type == fmt.Type.OBJECT:
        thm.face_count = packed_reader.getf('<I')[0]
        thm.vertex_count = packed_reader.getf('<I')[0]

    elif thm.file_type == fmt.Type.TEXTURE:
        thm.material = packed_reader.getf('<I')[0]
        thm.material_weight = packed_reader.getf('<f')[0]

    else:
        print('unsupported *.thm params')


def read_bump(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    thm.bump_virtual_height = packed_reader.getf('<f')[0]
    thm.bump_mode = packed_reader.getf('<I')[0]
    thm.bump_name = packed_reader.gets()


def read_ext_normalmap(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    thm.ext_normal_map_name = packed_reader.gets()


def read_texture_param(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    thm.texture_format = packed_reader.getf('<I')[0]
    thm.flags = packed_reader.getf('<I')[0]
    thm.border_color = packed_reader.getf('<I')[0]
    thm.fade_color = packed_reader.getf('<I')[0]
    thm.fade_amount = packed_reader.getf('<I')[0]
    thm.mip_filter = packed_reader.getf('<I')[0]
    thm.width = packed_reader.getf('<I')[0]
    thm.height = packed_reader.getf('<I')[0]


def read_texture_type(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    thm.texture_type = packed_reader.getf('<I')[0]


def read_detail_ext(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    thm.detail_name = packed_reader.gets()
    thm.detail_scale = packed_reader.getf('<f')[0]


def read_fade_delay(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    thm.fade_delay = packed_reader.getf('<B')[0]


def read_sound_param(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    thm.quality = packed_reader.getf('<f')[0]
    thm.min_dist = packed_reader.getf('<f')[0]
    thm.max_dist = packed_reader.getf('<f')[0]
    thm.game_type = packed_reader.getf('<I')[0]


def read_sound_param_2(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    thm.base_volume = packed_reader.getf('<f')[0]


def read_sound_ai_dist(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    thm.max_ai_dist = packed_reader.getf('<f')[0]


def read_group_param(data, thm):
    packed_reader = external.xray_io.PackedReader(data)

    objects_count = packed_reader.getf('<I')[0]

    for object_index in range(objects_count):
        object_name = packed_reader.gets()

        thm.objects_names.append(object_name)
