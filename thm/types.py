class Thumbnail:
    def set_version(self, version):
        self.version = version

    def set_type(self, thm_type):
        self.file_type = thm_type


class ThumbnailData(Thumbnail):
    def set_data(self, data):
        self.data = data


class ThumbnailSound(Thumbnail):
    def set_params(self, quality, min_dist, max_dist, game_type):
        self.quality = quality
        self.min_dist = min_dist
        self.max_dist = max_dist
        self.game_type = game_type

    def set_params_2(self, base_volume):
        self.base_volume = base_volume

    def set_ai_dist(self, max_ai_dist):
        self.max_ai_dist = max_ai_dist


class ThumbnailGroup(ThumbnailData):
    def __init__(self):
        self.objects_names = []

    def set_object_name(self, object_name):
        self.objects_names.append(object_name)


class ThumbnailObject(ThumbnailData):
    def set_object_param(self, face_count, vertex_count):
        self.face_count = face_count
        self.vertex_count = vertex_count


class ThumbnailTexture(ThumbnailData):
    def set_texture_param(
            self,
            texture_format,
            flags,
            border_color,
            fade_color,
            fade_amount,
            mip_filter,
            width,
            height
        ):
        self.texture_format = texture_format
        self.flags = flags
        self.border_color = border_color
        self.fade_color = fade_color
        self.fade_amount = fade_amount
        self.mip_filter = mip_filter
        self.width = width
        self.height = height

    def set_texture_type(self, texture_type):
        self.texture_type = texture_type

    def set_detail_ext(self, detail_name, detail_scale):
        self.detail_name = detail_name
        self.detail_scale = detail_scale

    def set_material(self, material, material_weight):
        self.material = material
        self.material_weight = material_weight

    def set_bump(self, bump_virtual_height, bump_mode, bump_name):
        self.bump_virtual_height = bump_virtual_height
        self.bump_mode = bump_mode
        self.bump_name = bump_name

    def set_ext_normal_map_name(self, ext_normal_map_name):
        self.ext_normal_map_name = ext_normal_map_name

    def set_fade_delay(self, fade_delay):
        self.fade_delay = fade_delay
