import os
from pathlib import Path

def update_tox_install(path):
    with open(path, 'r') as f:
        content = f.read()

    # The block we are looking for is:
    #       - name: Install tox
    #         run: python -m pip install tox

    # Replace with:
    #       - name: Install tox
    #         run: python -m pip install tox coverage

    content = content.replace("python -m pip install tox\n", "python -m pip install tox coverage\n")

    with open(path, 'w') as f:
        f.write(content)

def main():
    projects_dir = Path("/home/jayaram/Projects")
    for action_file in projects_dir.rglob("run-tests.yml*"):
        if ".venv" in str(action_file) or ".tox" in str(action_file) or "trash" in str(action_file):
            continue
            
        update_tox_install(action_file)

if __name__ == "__main__":
    main()
