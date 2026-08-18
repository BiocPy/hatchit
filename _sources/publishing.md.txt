# Publishing Process

## GitHub
Push your generated code to GitHub. The included workflows (`run-tests.yml` and `publish-pypi.yml`) will automatically begin checking your tests on every push.

## Zenodo & Citations
Ensure you've activated Zenodo for your repository. Because `hatchit` generates a `.zenodo.json` file, your GitHub releases will automatically mint DOIs! 
You will also find a `CITATION.cff` file at the root. Be sure to replace the placeholder fields before your first release so GitHub enables the "Cite this repository" button.

## PyPI
The scaffold includes PyPI Trusted Publishing integration. Once you configure your GitHub repository environment in PyPI, creating a new GitHub Release will automatically securely publish your wheel to PyPI.
