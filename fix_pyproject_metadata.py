import os
import tomllib
from pathlib import Path
import re

def process_pyproject(path):
    with open(path, 'r') as f:
        content = f.read()
    
    try:
        data = tomllib.loads(content)
    except Exception as e:
        print(f"Failed to parse TOML {path}: {e}")
        return
        
    project_data = data.get('project', {})
    org_name = path.parent.parent.name
    repo_name = path.parent.name
    
    # Capitalization logic for GitHub URL conventions
    if org_name == "biocpy":
        org_url = "BiocPy"
    else:
        org_url = org_name

    # 1. Keywords
    if "keywords" not in project_data:
        # insert after requires-python
        keyword_str = 'keywords = [\n    "bioinformatics",\n]\n'
        content = re.sub(r'(requires-python = ".*?"\n)', r'\1' + keyword_str, content)
        
    # 2. Classifiers
    if "classifiers" not in project_data:
        classifier_str = """classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
    "Typing :: Typed",
]
"""
        # insert after requires-python or keywords
        if "keywords = [" in content:
            # find end of keywords block
            content = re.sub(r'(keywords = \[.*?\]\n)', r'\1' + classifier_str, content, flags=re.DOTALL)
        else:
            content = re.sub(r'(requires-python = ".*?"\n)', r'\1' + classifier_str, content)

    # 3. License
    if "license" not in project_data:
        # inject [project.license] block before [project.optional-dependencies] or [build-system]
        license_str = '\n[project.license]\nfile = "LICENSE.txt"\n'
        if "[project.urls]" in content:
            content = content.replace("[project.urls]", license_str + "\n[project.urls]")
        elif "[project.optional-dependencies]" in content:
            content = content.replace("[project.optional-dependencies]", license_str + "\n[project.optional-dependencies]")
        else:
            content = content.replace("[build-system]", license_str + "\n[build-system]")

    # 4. URLs
    if "urls" not in project_data:
        urls_str = f"""\n[project.urls]
Homepage = "https://github.com/{org_url}/{repo_name}"
Documentation = "https://{org_url.lower()}.github.io/{repo_name}/"
Source = "https://github.com/{org_url}/{repo_name}"
"Bug Tracker" = "https://github.com/{org_url}/{repo_name}/issues"
"""
        if "[project.optional-dependencies]" in content:
            content = content.replace("[project.optional-dependencies]", urls_str + "\n[project.optional-dependencies]")
        else:
            content = content.replace("[build-system]", urls_str + "\n[build-system]")

    with open(path, 'w') as f:
        f.write(content)


def main():
    projects_dir = Path("/home/jayaram/Projects")
    for pyproj in projects_dir.rglob("pyproject.toml"):
        if ".venv" in str(pyproj) or ".tox" in str(pyproj) or "trash" in str(pyproj):
            continue
        
        # Ensure it has a standard build system to avoid touching random pyprojects
        with open(pyproj, 'r') as f:
            if "hatchling" not in f.read() and "setuptools" not in f.read():
                continue
                
        print(f"Fixing metadata for {pyproj}")
        process_pyproject(pyproj)

if __name__ == "__main__":
    main()
