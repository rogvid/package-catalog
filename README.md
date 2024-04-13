# Python package catalog

A catalog of python packages

## Usage

TBW

## Setup

### Dependencies

- python
- poetry [pip]
- make (optional)
- pytest (optional, installed by poetry, but it's more convenient to have it installed on the system) [pip]
- pre-commit (optional, installed by poetry, but it's more convenient to have it installed on the system) [pip]

### Development Environment Configuration

- Configure the project (poetry, pre-commit):
  ```bash
  make setup
  ```
  or to have more strict pre-commit rules:
  ```bash
  make setup-strict
  ```
- Open VSCode and install the suggested extensions

#### Environment Variables

##### Development

Project specific environment variables are defined in the `.env` file. This file is not versioned and it's used for local development only. If you would like these to automatically be loaded, it is recommended that you install direnv and run `direnv allow`, which will then also automatically load the poetry virtual environment using the `layout_poetry` functionality in the `.envrc` file.

##### Production

For production it is not recommended to use a `.envrc` file or direnv.

## Versioning

This project is tagged with versions according to [SemVer](https://semver.org/). To bump the project version:

```bash
make bump
```
