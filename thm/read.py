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
