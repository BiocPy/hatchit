import os
import glob
from pathlib import Path
import re

def fix_pyproject_toml(path):
    if not path.exists(): return
    with open(path, 'r') as f:
        content = f.read()
    
    # We replaced [dependency-groups] with [project.optional-dependencies]
    # But if it had [project.optional-dependencies] earlier, it's invalid.
    
    # Let's check if there are two [project.optional-dependencies]
    if content.count("[project.optional-dependencies]") > 1:
        # We need to extract the second block (which was dev = [...])
        # and move it to the first block.
        
        # 1. Find the second block
        # It's at the end of the file in our case, but let's be robust
        parts = content.split("[project.optional-dependencies]")
        
        # parts[0] is everything before first block
        # parts[1] is the first block
        # parts[2] is the second block (dev)
        
        # We want to append parts[2] to parts[1]
        
        new_content = parts[0] + "[project.optional-dependencies]" + parts[1].rstrip() + "\n" + parts[2].lstrip()
        
        with open(path, 'w') as f:
            f.write(new_content)
            
def main():
    projects_dir = Path("/home/jayaram/Projects")
    for pyproj in projects_dir.rglob("pyproject.toml"):
        if ".venv" in str(pyproj) or ".tox" in str(pyproj) or "trash" in str(pyproj):
            continue
        
        try:
            fix_pyproject_toml(pyproj)
            # test validity
            import tomllib
            with open(pyproj, 'rb') as f:
                tomllib.load(f)
        except Exception as e:
            print(f"Failed on {pyproj}: {e}")

if __name__ == "__main__":
    main()
