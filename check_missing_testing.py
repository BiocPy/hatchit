import os
from pathlib import Path

projects_dir = Path("/home/jayaram/Projects")
missing_testing = []

for pyproj in projects_dir.rglob("pyproject.toml"):
    if ".venv" in str(pyproj) or ".tox" in str(pyproj) or "trash" in str(pyproj):
        continue
    
    with open(pyproj, 'r') as f:
        content = f.read()
        
    # only care if we just migrated it - we can tell if it has tox.ini with `extras = testing`
    tox_file = pyproj.parent / "tox.ini"
    if tox_file.exists():
        with open(tox_file, 'r') as tf:
            tox_content = tf.read()
            if "extras = testing" in tox_content:
                if "\ntesting =" not in content and "\ntesting=" not in content:
                    missing_testing.append(str(pyproj))

for p in sorted(missing_testing):
    print(p)
