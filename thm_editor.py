
import sys
import os

import thm


external_modules_path = os.path.abspath(os.curdir)
sys.path.append(external_modules_path)
thm_file_path = sys.argv[1]
thm.main(thm_file_path)
