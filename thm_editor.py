
import sys
import os


external_modules_path = os.path.join(os.path.abspath(os.curdir), 'external')
io_scene_xray_path = os.path.join(external_modules_path, 'blender-xray' + os.sep + 'io_scene_xray')
sys.path.append(io_scene_xray_path)


import thm
