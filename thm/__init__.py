from . import thm
from . import ui


def main(thm_file_path):
    thumbnail = thm.read_thm(thm_file_path)
    ui.create_main_window(thumbnail)
