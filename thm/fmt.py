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
    SOUND_PARAM         = 0x1000
    SOUND_BASE_VOLUME   = 0x1001
    SOUND_AI_DIST       = 0x1002


class ThmGroupChunks:
    GROUP_PARAM     = 0x0001


class Type:
    OBJECT          = 0
    TEXTURE         = 1
    SOUND           = 2
    GROUP           = 3

    SUPPORTED       = (OBJECT, TEXTURE, SOUND, GROUP)


class TextureFormat:
    DXT1_RGB    =  0
    DXT1_ARGB   =  1
    DXT3_ARGB   =  2
    DXT5_ARGB   =  3
    RGB_4444    =  4
    ARGB_1555   =  5
    RGB_565     =  6
    RGB         =  7
    RGBA        =  8
    NVHS        =  9
    NVHU        = 10
    A8          = 11
    L8          = 12
    A8L8        = 13


tex_fmt_names = {
    TextureFormat.DXT1_RGB:   'DXT1',
    TextureFormat.DXT1_ARGB:  'DXT1 Alpha',
    TextureFormat.DXT3_ARGB:  'DXT3',
    TextureFormat.DXT5_ARGB:  'DXT5',
    TextureFormat.RGB_4444:   '16 Bit (4:4:4:4)',
    TextureFormat.ARGB_1555:  '16 Bit (1:5:5:5)',
    TextureFormat.RGB_565:    '16 Bit (5:6:5)',
    TextureFormat.RGB:        '24 Bit (8:8:8)',
    TextureFormat.RGBA:       '32 Bit (8:8:8:8)',
    TextureFormat.NVHS:       'NVHS',
    TextureFormat.NVHU:       'NVHU',
    TextureFormat.A8:         '8 Bit (Alpha)',
    TextureFormat.L8:         '8 Bit (Luminance)',
    TextureFormat.A8L8:       '16 Bit (Alpha:Luminance)'
}


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
