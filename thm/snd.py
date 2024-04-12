def read_sound_param(packed_reader, thm):
    thm.quality     = packed_reader.getf('<f')[0]
    thm.min_dist    = packed_reader.getf('<f')[0]
    thm.max_dist    = packed_reader.getf('<f')[0]
    thm.game_type   = packed_reader.getf('<I')[0]


def read_sound_base_volume(packed_reader, thm):
    thm.base_volume = packed_reader.getf('<f')[0]


def read_sound_ai_dist(packed_reader, thm):
    thm.max_ai_dist = packed_reader.getf('<f')[0]
