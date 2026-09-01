from pathlib import Path

projects_dir = Path("/home/jayaram/Projects")
for tox in projects_dir.rglob("tox.ini"):
    if ".venv" in str(tox) or ".tox" in str(tox) or "trash" in str(tox):
        continue
        
    with open(tox, 'r') as f:
        content = f.read()
        
    original = content
    content = content.replace("uv run --all-extras ", "")
    content = content.replace("uv run ", "")
    
    if content != original:
        with open(tox, 'w') as f:
            f.write(content)
            
