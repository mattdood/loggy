# loggy
A simple logging utility.

<img src="https://img.shields.io/github/issues/mattdood/loggy"
    target="https://github.com/mattdood/loggy/issues"
    alt="Badge for GitHub issues."/>
<img src="https://img.shields.io/github/forks/mattdood/loggy"
    target="https://github.com/mattdood/loggy/forks"
    alt="Badge for GitHub forks."/>
<img src="https://img.shields.io/github/stars/mattdood/loggy"
    alt="Badge for GitHub stars."/>
<img src="https://img.shields.io/github/license/mattdood/loggy"
    target="https://github.com/mattdood/loggy/raw/master/LICENSE"
    alt="Badge for GitHub license, MIT."/>
<img src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fmattdood%2Floggy"
    target="https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fmattdood%2Floggy"
    alt="Badge for sharable Twitter link."/>
[![Pytest](https://github.com/mattdood/loggy/actions/workflows/ci.yml/badge.svg)](https://github.com/mattdood/loggy/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/loggy.svg)](https://badge.fury.io/py/loggy)

## Installation
To install the package locally use the following:

```
pip install get-loggy
```

## Features
* Color support
* Custom color support (advanced)
* Add additional logging levels
* Optional log stream vs. log file
* Log record format
* Package level logging

## Usage
Loggy exists as a simple interface for some standard logging in Python.
This is done at the package level, not by name.

```
from loggy import loggy

log = loggy.get_loggy()

log.info("Something")

>>> 2022-06-21 20:16:39 PM PDT | INFO | something | (<stdin>:1:<module>) |
```

## Advanced usage
Custom colors can be created or added along with custom logging levels.
See the [`conftest.py`](./conftest.py) for an example.

## Initial setup
The following GitHub secrets will need to be added in order to release the PyPI
packages without the CI failing:
* `TEST_PYPI_API_TOKEN`
* `PYPI_API_TOKEN`

These can be generated using the following links:
* [PyPI](https://pypi.org/manage/account/token/)
* [Test PyPI](https://test.pypi.org/manage/account/token/)

## Running tests
[Pytest](https://pytest.org) is used as the test runner. To install and run tests
use the `requirements-dev.txt` and execute with `pytest`.

**Note:** Use a virtual environment. The steps to create one are left to the user,
there are many packages that accomplish this.

```bash
pip install -r requirements-dev.txt
pytest
```

