# Contributing to the package

## Development Environment

First create a virtual environment:

```bash
python -m venv venv
```

If the venv is not activated automatically, run:

```bash
venv\Scripts\activate
```

You can simply install the package in editable mode from inside the venv:

```bash
pip install -e .
```

This will also install the required packages listed in [setup.cfg](setup.cfg) as `install_requires`.

But consider that changes to the setup files are only applied if you reinstall the package.

If you want to create the package run:

```bash
python setup.py sdist
```

This project uses tox to run different environments:

* testenv:
  * pytest
  * pylint
  * coverage
  * mypy

So in order to run the test simply install tox in your venv:

```bash
pip install tox
```

After that just run
```bash
tox
```

Look at the [tox.ini](tox.ini) file at the [testenv] section if you want to know what
is executed inside the tox environment and which python versions are tested.

The example output for a successfull run below:
```bash

```
