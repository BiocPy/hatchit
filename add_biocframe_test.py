import re
from pathlib import Path

pyproj = Path("/home/jayaram/Projects/biocpy/biocutils/pyproject.toml")
with open(pyproj, "r") as f:
    content = f.read()

content = content.replace('"pandas>=3.0.5",\n', '"pandas>=3.0.5",\n    "biocframe",\n    "iranges",\n')

with open(pyproj, "w") as f:
    f.write(content)
