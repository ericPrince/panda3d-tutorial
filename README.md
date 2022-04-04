# panda3d tutorial

```bash
pip install my-package
```

## Developer Install

Use pipenv to create a virtual environment. Then install the
git pre-commit hooks.

```bash
pipenv --python=3.10  # or whatever python version you want
pipenv install --dev
pipenv run pre-commit install
```

You can activate the virtual environment so you don't need to prefix
every command with `pipenv run`:

```bash
source $(dirname $(pipenv run which python))/activate
```
