import os
import glob
from pathlib import Path
import re

def fix_tox(path):
    if not path.exists(): return
    with open(path, 'r') as f:
        content = f.read()
    
    # split by testenv blocks
    blocks = re.split(r'(\[testenv\]|\[testenv:.*?\])', content)
    
    for i in range(1, len(blocks), 2):
        header = blocks[i]
        body = blocks[i+1]
        
        if header == "[testenv]":
            # Remove skip_install = True
            body = body.replace("skip_install = True\n", "")
            # Change extras = dev to extras = testing
            body = body.replace("extras = dev", "extras = testing")
        
        blocks[i+1] = body
        
    new_content = "".join(blocks)
    with open(path, 'w') as f:
        f.write(new_content)

def fix_pyproject(path):
    if not path.exists(): return
    with open(path, 'r') as f:
        content = f.read()
        
    # We want to remove the 'dev = [...]' block inside project.optional-dependencies 
    # if it's at the end of the file. 
    # Or actually, we can just remove it using regex since it looks like:
    # dev = [
    #     ...
    # ]
    
    # A safer way is to just find [project.optional-dependencies]\ndev = [ ... ]
    # and remove it if it exists.
    # It might be just `dev = [ ... ]` at the end of the file if we merged it earlier.
    
    # We can just read the lines, and if we encounter `dev = [`, we delete until `]`
    lines = content.split('\n')
    new_lines = []
    in_dev = False
    
    for line in lines:
        if line.startswith("dev = ["):
            in_dev = True
            continue
        if in_dev:
            if line.strip() == "]":
                in_dev = False
            continue
        new_lines.append(line)
        
    with open(path, 'w') as f:
        f.write('\n'.join(new_lines))

def main():
    projects_dir = Path("/home/jayaram/Projects")
    for tox in projects_dir.rglob("tox.ini"):
        if ".venv" in str(tox) or ".tox" in str(tox) or "trash" in str(tox):
            continue
        fix_tox(tox)
        
    for pyproj in projects_dir.rglob("pyproject.toml"):
        if ".venv" in str(pyproj) or ".tox" in str(pyproj) or "trash" in str(pyproj):
            continue
        fix_pyproject(pyproj)

if __name__ == "__main__":
    main()
