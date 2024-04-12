class ThmChunks:
    VERSION         = 0x0810
    DATA            = 0x0811
    TYPE            = 0x0813


class ThmObjectChunks:
    OBJECT_PARAM    = 0x0816


class ThmTextureChunks:
    TEXTURE_PARAM   = 0x0812
    TEXTURE_TYPE    = 0x0814
    DETAIL_EXT      = 0x0815
    MATERIAL        = 0x0816
    BUMP            = 0x0817
    EXT_NORMALMAP   = 0x0818
    FADE_DELAY      = 0x0819


class ThmSoundChunks:
    SOUND_PARAM     = 0x1000
    SOUND_PARAM_2   = 0x1001
    SOUND_AI_DIST   = 0x1002


class ThmGroupChunks:
    GROUP_PARAM     = 0x0001


class Type:
    OBJECT          = 0
    TEXTURE         = 1
    SOUND           = 2
    GROUP           = 3

    SUPPORTED       = (OBJECT, TEXTURE, SOUND, GROUP)


class Version:
    OBJECT          = 18
    TEXTURE         = 18
    SOUND           = 20
    GROUP           =  1

    SUPPORTED       = (OBJECT, TEXTURE, SOUND, GROUP)


THUMB_WIDTH         = 128
THUMB_HEIGHT        = 128
THUMB_PIXELS_COUNT  = THUMB_HEIGHT * THUMB_WIDTH
THUMB_SIZE          = THUMB_PIXELS_COUNT * 4
