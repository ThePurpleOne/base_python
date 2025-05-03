Template for a **typed-checked**, **lint-ed**, and **formatted** Python project.

Setup using the standard `pyproject.toml` and managed via [Astral uv](https://docs.astral.sh/uv/)

It sets up:
- [Astral uv](https://docs.astral.sh/uv/)
- [Pyright](https://github.com/microsoft/pyright) Type Checker
- [Ruff](https://docs.astral.sh/ruff/) Linter and Formatter
- [pre-commit](https://pre-commit.com/)
- [pytest](https://pypi.org/project/pytest/)

Run code
```bash
uv run src/main.py
```

# Needed tools
You'll need some tools to be able to use the environment properly.

## Astral uv
[https://docs.astral.sh/uv/getting-started/installation](https://docs.astral.sh/uv/getting-started/installation)

On windows:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

On mac or linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## act

Act is a tool to run GitHub Actions locally. It's not mandatory, but it's very useful to test the CI pipeline locally.

Follow the instructions to install it on your system:
[https://nektosact.com/installation/index.html](https://nektosact.com/installation/index.html)

# Using the environment

## Pre-commit

Run pre-commit hooks, that will **format**, **lint** and type check your code 
```bash
uv run pre-commit run --all-files
```

## Unit Tests
This step is not included in the pre-commit hooks to avoid disrupting the developer's workflow and to encourage frequent commits

Run tests
```bash
uv run pytest -v
```

## Linting and Formatting by hand

This is already done by pre-commit, but you can run it manually if you want to.
Run formatter
```bash
uv run ruff format .
```

Run linter
```bash
uv run ruff check .
```

## Type Checking
It is ran in the CI pipeline, but you can run it locally if you want to.

Run type checker
```bash
uv run pyright
```

Run the CI locally using [act](https://github.com/nektos/act)
```bash
act
```


