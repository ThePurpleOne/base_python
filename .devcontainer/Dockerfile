FROM mcr.microsoft.com/devcontainers/python:3.11

# Install uv and use it to install tools into the global environment
RUN pip install uv && \
    uv pip install --system pyright ruff pre-commit
