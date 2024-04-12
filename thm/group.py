def read_group_param(packed_reader, thm):
    objects_count = packed_reader.getf('<I')[0]

    for object_index in range(objects_count):
        object_name = packed_reader.gets()

        thm.objects_names.append(object_name)
