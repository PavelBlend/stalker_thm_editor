from . import fmt


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
    thm.tex_format_id   = packed_reader.getf('<I')[0]
    thm.tex_format      = fmt.tex_fmt_names.get(thm.tex_format_id, 'Unknown')
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
