ARG BASE_IMAGE=python:3.11.4-slim-bullseye
FROM ${BASE_IMAGE}

ARG USER_NAME=api
ARG GROUP_NAME=apis
ARG UID=1000
ARG GID=1000
ARG APPLICATION_DIRECTORY=/app/src
ARG RUN_POETRY_INSTALL_AT_BUILD_TIME="false"

ENV DEBIAN_FRONTEND="noninteractive" \
    LC_ALL="C.UTF-8" \
    LANG="C.UTF-8" \
    PYTHONPATH=${APPLICATION_DIRECTORY}

RUN apt update && apt install --no-install-recommends -y \
    git curl make

RUN python3 -m pip install --upgrade pip setuptools requests \
    && python3 -m pip install poetry

RUN groupadd -g ${GID} ${GROUP_NAME} \
    && useradd -ms /bin/sh -u ${UID} -g ${GID} ${USER_NAME}

USER ${USER_NAME}
WORKDIR ${APPLICATION_DIRECTORY}

# COPY --chown=${UID}:${GID} pyproject.toml poetry.lock poetry.toml ./
# CMD [ "bash" ]