def read_obj_params(packed_reader, thm):
    thm.face_count      = packed_reader.getf('<I')[0]
    thm.vertex_count    = packed_reader.getf('<I')[0]
