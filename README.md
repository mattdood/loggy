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

## Linting code
The project utilizes [Pre-Commit](https://pre-commit.com) to execute linting. This
ensures code quality is solid, and is used both in the CI and the `requirements-dev.txt`
for local execution.

The following hooks are used inside Pre-Commit:
* trailing-whitespace
* check-yaml
* isort
* flake8

To run Pre-Commit, use the following:

```bash
pre-commit run --all-files
```

## Releasing builds
To release builds for the project we use a combination of tagging and changes to
`setup.py`.

For any releases to [test.pypi.org](https://test.pypi.org) use a change to the
`version="..."` inside of `setup.py`. Once a PR is merged into the main project
the test release will be updated.

Any prod releases to [pypi.org](https://pypi.org) require a tagged version number.
This should be done locally by running the following:

```bash
git checkout master
git pull master
git tag v<version-number-here>
git push origin v<version-number-here>
```

### Rollbacks of versions
To roll a version back we need to delete the tagged release from the prod PyPI,
then delete the GitHub tag.

```
git tag -d v<version-number-here>
git push origin :v<version-number-here>
```

