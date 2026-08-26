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

## What's Next? (After Setup Checklist)

Now that your project is perfectly scaffolded, there are just a few quick things you'll want to configure to get the full automated experience working for you:

1. **Update `pyproject.toml` keywords**: We've added a few placeholder keywords (like `"TODO"`, `"FIXME"`) to your `pyproject.toml`. Swap those out with relevant keywords for your package to make it more discoverable on PyPI!
2. **Setup PyPI Trusted Publishing**: We use GitHub Actions for publishing. You don't need any secrets! Instead, head over to PyPI, create a "Pending Publisher", and link it to your GitHub repository. [Read more here](https://docs.pypi.org/trusted-publishers/).
3. **Configure Codecov (Optional)**: If you want test coverage reports, head to [Codecov](https://about.codecov.io/), link your repo, grab your token, and add it as a `CODECOV_TOKEN` secret in your GitHub repository.
4. **Activate pre-commit.ci (Optional)**: If you want automated PRs keeping your code perfectly formatted, enable the [pre-commit.ci](https://pre-commit.ci/) bot on your repo.
5. **Enable GitHub Pages (Optional)**: The publishing workflow automatically builds your Sphinx docs. To serve them, go to your repository settings, navigate to "Pages", and select **GitHub Actions** as the "Source". The deployment workflow will automatically publish the built artifact to your site!

That's it! You're ready to start writing code.

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
