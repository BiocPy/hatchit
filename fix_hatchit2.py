import sys
from pathlib import Path

# Load functions from our existing scripts
import imp
fix_tox_ini = imp.load_source('fix_tox_ini', 'fix_tox_ini.py')
fix_tox_skip_install = imp.load_source('fix_tox_skip_install', 'fix_tox_skip_install.py')

root = Path("/home/jayaram/Projects/biocpy/hatchit")
fix_tox_ini.fix_tox(root / "tox.ini")
fix_tox_skip_install.fix_tox(root / "tox.ini")
fix_tox_skip_install.fix_pyproject(root / "pyproject.toml")
