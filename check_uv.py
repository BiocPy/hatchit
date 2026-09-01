import os
import glob
from pathlib import Path

projects_dir = Path("/home/jayaram/Projects")
uv_projects = []

for pyproj in projects_dir.rglob("pyproject.toml"):
    if ".venv" in str(pyproj) or ".tox" in str(pyproj):
        continue
    
    project_root = pyproj.parent
    workflows_dir = project_root / ".github" / "workflows"
    run_tests = workflows_dir / "run-tests.yml"
    
    if run_tests.exists():
        with open(run_tests, 'r') as f:
            if 'setup-uv' in f.read():
                uv_projects.append(str(project_root))

print("Projects using uv:")
for p in sorted(uv_projects):
    print(p)
