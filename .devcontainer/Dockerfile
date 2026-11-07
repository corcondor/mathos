FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl gh git python3 ripgrep util-linux zstd \
    && rm -rf /var/lib/apt/lists/*
