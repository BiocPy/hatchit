from pathlib import Path

paths = [
    Path("/home/jayaram/Projects/biocpy/biostrings/pyproject.toml"),
    Path("/home/jayaram/Projects/biocpy/iranges/pyproject.toml")
]

for p in paths:
    if not p.exists(): continue
    with open(p, 'r') as f:
        content = f.read()
    
    if "testing = [" not in content:
        content = content.replace("[project.optional-dependencies]", 
                                  "[project.optional-dependencies]\ntesting = [\n    \"pytest>=9.1.1\",\n    \"pytest-cov>=7.1.0\",\n]\n")
        with open(p, 'w') as f:
            f.write(content)

