import os
from pathlib import Path
import re

def create_docs_requirements(repo_root):
    docs_dir = repo_root / "docs"
    docs_dir.mkdir(exist_ok=True)
    req_file = docs_dir / "requirements.txt"
    if not req_file.exists():
        req_file.write_text("sphinx>=7.0.0\nfuro\nmyst-nb\nsphinx-autodoc-typehints\nlinkify-it-py\n")

def fix_tox(path):
    if not path.exists(): return
    with open(path, 'r') as f:
        content = f.read()
    
    # split by testenv blocks
    blocks = re.split(r'(\[testenv\]|\[testenv:.*?\])', content)
    
    for i in range(1, len(blocks), 2):
        header = blocks[i]
        body = blocks[i+1]
        
        if header == "[testenv:typecheck]":
            body = body.replace("skip_install = True\n", "")
            if "extras = dev\n" in body:
                body = body.replace("extras = dev\n", "deps = mypy\n")
            elif "extras = testing\n" in body:
                body = body.replace("extras = testing\n", "deps = mypy\n")
            elif "deps = mypy" not in body:
                # Add deps = mypy after the description or at the beginning
                if "description =" in body:
                    body = body.replace("description =", "deps = mypy\ndescription =", 1)
                else:
                    body = "deps = mypy\n" + body
                    
        elif "docs" in header and "linkcheck" in header: # [testenv:{docs,doctests,linkcheck}]
            body = body.replace("skip_install = True\n", "")
            if "extras = dev\n" in body:
                body = body.replace("extras = dev\n", "")
            elif "extras = testing\n" in body:
                body = body.replace("extras = testing\n", "")
                
            if "deps =" not in body:
                deps_str = "deps =\n    -r {toxinidir}/docs/requirements.txt\n"
                if "setenv =" in body:
                    body = body.replace("setenv =", deps_str + "setenv =", 1)
                else:
                    body = deps_str + body
            
            # create the requirements.txt file for this repo if it's missing
            repo_root = path.parent
            create_docs_requirements(repo_root)

        blocks[i+1] = body
        
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
