# hatchit 🚀

A modern, Python project scaffolder combining the blazing speed of `uv` with the robust build ecosystem of `hatch`. 

Inspired by PyScaffold, `hatchit` scaffolds Python packages, fully equipped with automated testing, documentation, and scientific publishing metadata.

## Setup & Installation

You must have `uv` installed on your system.

```bash
pip install hatchit
```

## Quickstart Tutorial

To create a brand new repository, you can use the `hatchit` CLI command:

```bash
hatchit my-awesome-package --description "A robust new tool" --license MIT
```

Alternatively, since `hatchit` is a 100% compatible Copier template, you can use `copier` directly to render the project!

```bash
pip install copier
copier copy https://github.com/biocpy/hatchit my-awesome-package
```

or to programmatically create a project,

```py
from hatchit import create_hatchit_repository
create_hatchit_repository(project_path = "my-awesome-package", description = "new tool", license = "MIT")
```

This will generate the project in the `my-awesome-package` directory and initialize a fresh Git repository.

## After setup

- The GitHub workflows use "trusted publisher workflow" to publish packages to PyPI. Read more instructions [here](https://docs.pypi.org/trusted-publishers/).
- Install [tox](https://tox.wiki/en/4.23.2/) to handle package tasks. GitHub Actions relies on the tox configuration to test, generate documentation, and publish packages.
- (Optional) Enable the [pre-commit.ci](https://pre-commit.ci/) bot for your repository.
- (Optional) Install [ruff](https://docs.astral.sh/ruff/) for code formatting.
- (Optional) Setup [codecov](https://about.codecov.io/) for coverage reports.


## Development Process

`hatchit` structures your project around `tox` and `uv`. To run your tests during development:

```bash
cd my-awesome-package
tox -e default
```

To build your documentation locally and preview:
```bash
tox -e docs
```

## Publishing Process

1. **GitHub Actions**: The included workflows will automatically begin checking your tests on all commits and PR's.
2. **PyPI**: Create a new GitHub Release or tag. The `publish-pypi.yml` workflow will automatically securely publish your wheel to PyPI via Trusted Publishing.
3. **Zenodo**: If you've activated Zenodo for your repository, `hatchit` includes a `.zenodo.json` and will automatically generate DOIs for new releases!
