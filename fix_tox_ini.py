import os
import glob
from pathlib import Path
import re

def fix_tox(path):
    if not path.exists(): return
    with open(path, 'r') as f:
        content = f.read()
    
    # split by testenv blocks
    blocks = re.split(r'(\[testenv:.*?\])', content)
    # blocks[0] is everything before the first [testenv:...]
    # blocks[1] is [testenv:...]
    # blocks[2] is the content of that block, etc.
    
    for i in range(1, len(blocks), 2):
        header = blocks[i]
        body = blocks[i+1]
        
        # Remove deps = twine from non-publish blocks
        if "publish" not in header:
            body = body.replace("deps = twine\n", "")
            
        # Also clean up any potential duplicate deps in publish itself?
        # A block might have two "deps = twine".
        # We can just deduplicate lines starting with deps =
        lines = body.split('\n')
        new_lines = []
        seen_deps = set()
        for line in lines:
            if line.startswith("deps ="):
                if line in seen_deps:
                    continue
                seen_deps.add(line)
            new_lines.append(line)
        blocks[i+1] = '\n'.join(new_lines)
        
    new_content = "".join(blocks)
    with open(path, 'w') as f:
        f.write(new_content)
        
def main():
    projects_dir = Path("/home/jayaram/Projects")
    for tox in projects_dir.rglob("tox.ini"):
        if ".venv" in str(tox) or ".tox" in str(tox) or "trash" in str(tox):
            continue
        fix_tox(tox)

if __name__ == "__main__":
    main()
