import re
from pathlib import Path

repo = Path("/home/jayaram/Projects/biocpy/biocutils")

# 1. Fix pyproject.toml
pyproj = repo / "pyproject.toml"
with open(pyproj, "r") as f:
    content = f.read()

# Remove the duplicate dev group
content = re.sub(r'\[project\.optional-dependencies\]\ndev = \[\n(    ".*?",\n)*\]\n?', '', content)
with open(pyproj, "w") as f:
    f.write(content.strip() + "\n")


# 2. Fix tox.ini
tox_ini = repo / "tox.ini"
tox_content = """# Tox configuration file
# Read more under https://tox.wiki/

[tox]
minversion = 4.0
envlist = default

[testenv]
description = Invoke pytest to run automated tests
extras = testing
commands =
    pytest {posargs}

[testenv:typecheck]
description = Run static type checking with mypy
deps = mypy
commands =
    mypy src/

[testenv:lint]
description = Perform static analysis and style checks
deps = ruff
skip_install = True
commands =
    ruff check {posargs:.}
    ruff format --check {posargs:.}

[testenv:{build,clean}]
description =
    build: Build the package
    clean: Remove old distribution files
deps = build
skip_install = True
commands =
    clean: python -c 'import shutil; [shutil.rmtree(p, True) for p in ("build", "dist", "docs/_build")]'
    clean: python -c 'import pathlib, shutil; [shutil.rmtree(p, True) for p in pathlib.Path("src").glob("*.egg-info")]'
    build: python -m build {posargs}

[testenv:{docs,doctests,linkcheck}]
description =
    docs: Invoke sphinx-build to build the docs
    doctests: Invoke sphinx-build to run doctests
    linkcheck: Check for broken links in the documentation
deps =
    -r {toxinidir}/docs/requirements.txt
setenv =
    DOCSDIR = {toxinidir}/docs
    BUILDDIR = {toxinidir}/docs/_build
    docs: BUILD = html
    doctests: BUILD = doctest
    linkcheck: BUILD = linkcheck
commands =
    sphinx-apidoc -f -o "{env:DOCSDIR}/api" src/
    sphinx-build --color -b {env:BUILD} -d "{env:BUILDDIR}/doctrees" "{env:DOCSDIR}" "{env:BUILDDIR}/{env:BUILD}" {posargs}

[testenv:publish]
description =
    Publish the package you have been developing to a package index server.
skip_install = True
deps = twine
commands =
    python -m twine upload {posargs:dist/*}
"""
with open(tox_ini, "w") as f:
    f.write(tox_content)

# 3. Fix run-tests.yml
run_tests = repo / ".github" / "workflows" / "run-tests.yml"
with open(run_tests, "r") as f:
    content = f.read()

content = re.sub(r'\n\s*- name: Set up uv\n\s*uses: astral-sh/setup-uv@v5\n\s*with:\n\s*enable-cache: true\n', '', content)
content = content.replace("uv tool install tox --with tox-uv", "python -m pip install tox")
content = re.sub(r'\n\s*- name: Install dependencies\n\s*run: uv sync --all-extras --python \$\{\{ matrix\.python \}\}\n', '', content)
with open(run_tests, "w") as f:
    f.write(content)

