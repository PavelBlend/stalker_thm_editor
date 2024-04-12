class Thumbnail:
    def __init__(self):
        self.version = None
        self.file_type = None


class ThumbnailData(Thumbnail):
    def __init__(self):
        super().__init__()
        self.data = None


class ThumbnailSound(Thumbnail):
    def __init__(self):
        super().__init__()
        self.quality = None
        self.min_dist = None
        self.max_dist = None
        self.game_type = None
        self.base_volume = None
        self.max_ai_dist = None
        self.base_volume = None
        self.max_ai_dist = None


class ThumbnailGroup(ThumbnailData):
    def __init__(self):
        super().__init__()
        self.objects_names = []


class ThumbnailObject(ThumbnailData):
    def __init__(self):
        super().__init__()
        self.face_count = None
        self.vertex_count = None


class ThumbnailTexture(ThumbnailData):
    def __init__(self):
        super().__init__()
        self.tex_format = None
        self.tex_format_id = None
        self.flags = None
        self.border_color = None
        self.fade_color = None
        self.fade_amount = None
        self.mip_filter = None
        self.width = None
        self.height = None
        self.texture_type = None
        self.detail_name = None
        self.detail_scale = None
        self.material = None
        self.material_weight = None
        self.bump_virtual_height = None
        self.bump_mode = None
        self.bump_name = None
        self.ext_normal_map_name = None
        self.fade_delay = None
