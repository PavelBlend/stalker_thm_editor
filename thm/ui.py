import os
import sys
import tkinter
from . import fmt


type_names = {
    0: 'Object',
    1: 'Texture',
    2: 'Sound'
}
type_names_list = ['Object', 'Texture', 'Sound']

SOUND_TYPE_NO_SOUND = 0x00000000

SOUND_TYPE_WEAPON = 0x80000000
SOUND_TYPE_ITEM = 0x40000000
SOUND_TYPE_MONSTER = 0x20000000
SOUND_TYPE_ANOMALY = 0x10000000
SOUND_TYPE_WORLD = 0x08000000

SOUND_TYPE_PICKING_UP = 0x04000000
SOUND_TYPE_DROPPING = 0x02000000
SOUND_TYPE_HIDING = 0x01000000
SOUND_TYPE_TAKING = 0x00800000
SOUND_TYPE_USING = 0x00400000

SOUND_TYPE_SHOOTING = 0x00200000
SOUND_TYPE_EMPTY_CLICKING = 0x00100000
SOUND_TYPE_BULLET_HIT = 0x00080000
SOUND_TYPE_RECHARGING = 0x00040000

SOUND_TYPE_DYING = 0x00020000
SOUND_TYPE_INJURING = 0x00010000
SOUND_TYPE_STEP = 0x00008000
SOUND_TYPE_TALKING = 0x00004000
SOUND_TYPE_ATTACKING = 0x00002000
SOUND_TYPE_EATING = 0x00001000

SOUND_TYPE_IDLE = 0x00000800

SOUND_TYPE_OBJECT_BREAKING = 0x00000400
SOUND_TYPE_OBJECT_COLLIDING = 0x00000200
SOUND_TYPE_OBJECT_EXPLODING = 0x00000100
SOUND_TYPE_AMBIENT = 0x00000080

SOUND_TYPE_ITEM_PICKING_UP = SOUND_TYPE_ITEM | SOUND_TYPE_PICKING_UP
SOUND_TYPE_ITEM_DROPPING = SOUND_TYPE_ITEM | SOUND_TYPE_DROPPING
SOUND_TYPE_ITEM_HIDING = SOUND_TYPE_ITEM | SOUND_TYPE_HIDING
SOUND_TYPE_ITEM_TAKING = SOUND_TYPE_ITEM | SOUND_TYPE_TAKING
SOUND_TYPE_ITEM_USING = SOUND_TYPE_ITEM | SOUND_TYPE_USING

SOUND_TYPE_WEAPON_SHOOTING = SOUND_TYPE_WEAPON | SOUND_TYPE_SHOOTING
SOUND_TYPE_WEAPON_EMPTY_CLICKING = SOUND_TYPE_WEAPON | SOUND_TYPE_EMPTY_CLICKING
SOUND_TYPE_WEAPON_BULLET_HIT = SOUND_TYPE_WEAPON | SOUND_TYPE_BULLET_HIT
SOUND_TYPE_WEAPON_RECHARGING = SOUND_TYPE_WEAPON | SOUND_TYPE_RECHARGING

SOUND_TYPE_MONSTER_DYING = SOUND_TYPE_MONSTER | SOUND_TYPE_DYING
SOUND_TYPE_MONSTER_INJURING = SOUND_TYPE_MONSTER | SOUND_TYPE_INJURING
SOUND_TYPE_MONSTER_STEP = SOUND_TYPE_MONSTER | SOUND_TYPE_STEP
SOUND_TYPE_MONSTER_TALKING = SOUND_TYPE_MONSTER | SOUND_TYPE_TALKING
SOUND_TYPE_MONSTER_ATTACKING = SOUND_TYPE_MONSTER | SOUND_TYPE_ATTACKING
SOUND_TYPE_MONSTER_EATING = SOUND_TYPE_MONSTER | SOUND_TYPE_EATING

SOUND_TYPE_ANOMALY_IDLE = SOUND_TYPE_ANOMALY | SOUND_TYPE_IDLE

SOUND_TYPE_WORLD_OBJECT_BREAKING = SOUND_TYPE_WORLD | SOUND_TYPE_OBJECT_BREAKING
SOUND_TYPE_WORLD_OBJECT_COLLIDING = SOUND_TYPE_WORLD | SOUND_TYPE_OBJECT_COLLIDING
SOUND_TYPE_WORLD_OBJECT_EXPLODING = SOUND_TYPE_WORLD | SOUND_TYPE_OBJECT_EXPLODING
SOUND_TYPE_WORLD_AMBIENT = SOUND_TYPE_WORLD | SOUND_TYPE_AMBIENT

SOUND_TYPE_WEAPON_PISTOL = SOUND_TYPE_WEAPON
SOUND_TYPE_WEAPON_GUN = SOUND_TYPE_WEAPON
SOUND_TYPE_WEAPON_SUBMACHINEGUN = SOUND_TYPE_WEAPON
SOUND_TYPE_WEAPON_MACHINEGUN = SOUND_TYPE_WEAPON
SOUND_TYPE_WEAPON_SNIPERRIFLE = SOUND_TYPE_WEAPON
SOUND_TYPE_WEAPON_GRENADELAUNCHER = SOUND_TYPE_WEAPON
SOUND_TYPE_WEAPON_ROCKETLAUNCHER = SOUND_TYPE_WEAPON

sg_Undefined = 0    # ???

sound_type_names = {
    sg_Undefined: "undefined",
    SOUND_TYPE_ITEM_PICKING_UP: "Item picking up",
    SOUND_TYPE_ITEM_DROPPING: "Item dropping",
    SOUND_TYPE_ITEM_TAKING: "Item taking",
    SOUND_TYPE_ITEM_HIDING: "Item hiding",
    SOUND_TYPE_ITEM_USING: "Item using",
    SOUND_TYPE_WEAPON_SHOOTING: "Weapon shooting",
    SOUND_TYPE_WEAPON_EMPTY_CLICKING: "Weapon empty clicking",
    SOUND_TYPE_WEAPON_BULLET_HIT: "Weapon bullet hit",
    SOUND_TYPE_WEAPON_RECHARGING: "Weapon recharging",
    SOUND_TYPE_MONSTER_DYING: "NPC dying",
    SOUND_TYPE_MONSTER_INJURING: "NPC injuring",
    SOUND_TYPE_MONSTER_STEP: "NPC step",
    SOUND_TYPE_MONSTER_TALKING: "NPC talking",
    SOUND_TYPE_MONSTER_ATTACKING: "NPC attacking",
    SOUND_TYPE_MONSTER_EATING: "NPC eating",
    SOUND_TYPE_ANOMALY_IDLE: "Anomaly idle",
    SOUND_TYPE_WORLD_OBJECT_BREAKING: "Object breaking",
    SOUND_TYPE_WORLD_OBJECT_COLLIDING: "Object colliding",
    SOUND_TYPE_WORLD_OBJECT_EXPLODING: "Object exploding",
    SOUND_TYPE_WORLD_AMBIENT: "World ambient"
}
sound_type_list_of_params = [
    "undefined",
    "Item picking up",
    "Item dropping",
    "Item taking",
    "Item hiding",
    "Item using",
    "Weapon shooting",
    "Weapon empty clicking",
    "Weapon bullet hit",
    "Weapon recharging",
    "NPC dying",
    "NPC injuring",
    "NPC step",
    "NPC talking",
    "NPC attacking",
    "NPC eating",
    "Anomaly idle",
    "Object breaking",
    "Object colliding",
    "Object exploding",
    "World ambient"
]


def draw_thumbnail(thm, img):
    bg_col = (127, 127, 127)    # background color

    for pixel_coord_x in range(fmt.THUMB_WIDTH):
        for pixel_coord_y in range(fmt.THUMB_HEIGHT):

            pixel_index = (pixel_coord_y * fmt.THUMB_WIDTH + pixel_coord_x)
            pixel = thm.data[pixel_index]

            alpha = pixel[3] / 255
            alpha_inv = 1.0 - alpha

            red = int(round(pixel[0] * alpha + bg_col[0] * alpha_inv, 0))
            green = int(round(pixel[1] * alpha + bg_col[1] * alpha_inv, 0))
            blue = int(round(pixel[2] * alpha + bg_col[2] * alpha_inv, 0))

            color = '#{:0>2x}{:0>2x}{:0>2x}'.format(blue, green, red)
            img.put(color, (pixel_coord_x, fmt.THUMB_HEIGHT - pixel_coord_y))


def create_main_window(thm):
    root = tkinter.Tk()
    root.title('STALKER Thumbnail Editor')

    row = 0

    # version
    version_label = tkinter.Label(root, text="Version")
    version_label.grid(row=row, column=0)
    version_value = tkinter.StringVar()
    version_value.set(thm.version)
    version_entry = tkinter.Entry(root, state=tkinter.DISABLED, textvariable=version_value, width=50)
    version_entry.grid(row=row, column=1)
    row += 1

    # type
    type_label = tkinter.Label(root, text="Type")
    type_label.grid(row=row, column=0)
    type_value = tkinter.StringVar()
    if thm.file_type == fmt.Type.OBJECT and thm.version == fmt.Version.GROUP:
        type_value.set('Group')
    else:
        type_value.set(type_names[thm.file_type])
    type_entry = tkinter.Entry(root, state=tkinter.DISABLED, textvariable=type_value, width=50)
    type_entry.grid(row=row, column=1)
    row += 1

    if thm.file_type == fmt.Type.OBJECT and thm.version == fmt.Version.OBJECT:

        face_count_label = tkinter.Label(root, text="Face Count")
        face_count_label.grid(row=row, column=0)
        face_count_value = tkinter.IntVar()
        face_count_value.set(thm.face_count)
        face_count_spinbox = tkinter.Entry(root, textvariable=face_count_value, state=tkinter.DISABLED, width=50)
        face_count_spinbox.grid(row=row, column=1)
        row += 1

        vert_count_label = tkinter.Label(root, text="Vert Count")
        vert_count_label.grid(row=row, column=0)
        vert_count_value = tkinter.IntVar()
        vert_count_value.set(thm.vertex_count)
        vert_count_spinbox = tkinter.Entry(root, textvariable=vert_count_value, state=tkinter.DISABLED, width=50)
        vert_count_spinbox.grid(row=row, column=1)
        row += 1

        data_label = tkinter.Label(root, text="Thumbnail")
        data_label.grid(row=row, column=0)
        img = tkinter.PhotoImage(width=fmt.THUMB_WIDTH, height=fmt.THUMB_HEIGHT)
        draw_thumbnail(thm, img)
        img_label = tkinter.Label(root, image=img)
        img_label.grid(row=row, column=1)
        row += 1

    elif thm.file_type == fmt.Type.OBJECT and thm.version == fmt.Version.GROUP:
        objects_label = tkinter.Label(root, text="Objects")
        objects_label.grid(row=row, column=0)
        row += 1
        for object_name in thm.objects_names:
            object_name_value = tkinter.StringVar()
            object_name_value.set(object_name)
            object_name_entry = tkinter.Entry(root, textvariable=object_name_value, state=tkinter.DISABLED, width=50)
            object_name_entry.grid(row=row, column=1)
            row += 1
        data_label = tkinter.Label(root, text="Thumbnail")
        data_label.grid(row=row, column=0)
        img = tkinter.PhotoImage(width=fmt.THUMB_WIDTH, height=fmt.THUMB_HEIGHT)
        draw_thumbnail(thm, img)
        img_label = tkinter.Label(root, image=img)
        img_label.grid(row=row, column=1)
        row += 1

    elif thm.file_type == fmt.Type.SOUND:

        quality_label = tkinter.Label(root, text="Quality")
        quality_label.grid(row=row, column=0)
        quality_value = tkinter.DoubleVar()
        quality_value.set(thm.quality)
        quality_spinbox = tkinter.Entry(root, textvariable=quality_value, width=50)
        quality_spinbox.grid(row=row, column=1)
        row += 1

        min_dist_label = tkinter.Label(root, text="Min Dist")
        min_dist_label.grid(row=row, column=0)
        min_dist_value = tkinter.DoubleVar()
        min_dist_value.set(thm.min_dist)
        min_dist_spinbox = tkinter.Entry(root, textvariable=min_dist_value, width=50)
        min_dist_spinbox.grid(row=row, column=1)
        row += 1

        max_dist_label = tkinter.Label(root, text="Max Dist")
        max_dist_label.grid(row=row, column=0)
        max_dist_value = tkinter.DoubleVar()
        max_dist_value.set(thm.max_dist)
        max_dist_spinbox = tkinter.Entry(root, textvariable=max_dist_value, width=50)
        max_dist_spinbox.grid(row=row, column=1)
        row += 1

        base_volume_label = tkinter.Label(root, text="Base Volume")
        base_volume_label.grid(row=row, column=0)
        base_volume_value = tkinter.DoubleVar()
        base_volume_value.set(thm.base_volume)
        base_volume_spinbox = tkinter.Entry(root, textvariable=base_volume_value, width=50)
        base_volume_spinbox.grid(row=row, column=1)
        row += 1

        max_ai_dist_label = tkinter.Label(root, text="Max AI Dist")
        max_ai_dist_label.grid(row=row, column=0)
        max_ai_dist_value = tkinter.DoubleVar()
        max_ai_dist_value.set(thm.max_ai_dist)
        max_ai_dist_spinbox = tkinter.Entry(root, textvariable=max_ai_dist_value, width=50)
        max_ai_dist_spinbox.grid(row=row, column=1)
        row += 1

        game_type_label = tkinter.Label(root, text="Game Type")
        game_type_label.grid(row=row, column=0)
        game_type_value = tkinter.StringVar()
        game_type_value.set(sound_type_names[thm.game_type])
        game_type_spinbox = tkinter.OptionMenu(root, game_type_value, *sound_type_list_of_params)
        game_type_spinbox.grid(row=row, column=1)
        row += 1

    elif thm.file_type == fmt.Type.TEXTURE:

        if getattr(thm, 'data', None):
            data_label = tkinter.Label(root, text="Thumbnail")
            data_label.grid(row=row, column=0)
            img = tkinter.PhotoImage(width=fmt.THUMB_WIDTH, height=fmt.THUMB_HEIGHT)
            draw_thumbnail(thm, img)
            img_label = tkinter.Label(root, image=img)
            img_label.grid(row=row, column=1)
            row += 1

    root.mainloop()
