import winreg, os, sys


subkey = 'Applications\\thm_editor.py\\shell\\open\\command'
# hkey = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, subkey, 0, winreg.KEY_WOW64_64KEY | winreg.KEY_ALL_ACCESS)
if 1:
    thm_editor_path = os.path.join(os.path.abspath(os.curdir), 'thm', 'associate.py')
    print(thm_editor_path)
    # python_exe_path = sys.executable
    # command = '{0} "{1}" %1 %*'.format(python_exe_path, thm_editor_path)
    # winreg.SetValue(winreg.HKEY_CLASSES_ROOT, subkey, winreg.REG_SZ, command)
    # hkey.Close()
input('ok')
