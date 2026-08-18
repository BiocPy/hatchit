# Development Process

`hatchit` structures your project around `tox` and `uv`. To run your tests during development:

```bash
cd my-awesome-package
tox -e default
```

To build your documentation locally and preview the Furo theme:
```bash
tox -e docs
```

You can add additional environments to `tox.ini` depending on your project needs. All dependency resolution is powered by `uv`.
