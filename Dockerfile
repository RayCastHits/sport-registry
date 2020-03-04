FROM python:3.7.5-alpine

WORKDIR /var/www/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install global packages
RUN apk update \
    && apk upgrade \
    && apk add --no-cache  \
    git \
    postgresql-dev \
    bash \
    libc-dev \
    libffi-dev \
    mariadb-dev \
    jpeg-dev \
    zlib-dev \
    gcc \
    python3-dev \
    nodejs \
    make \
    npm \
    yarn
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN yarn global add @vue/cli

# install frontend packages
COPY package.json package.json
COPY yarn.lock yarn.lock
RUN set -ex && yarn

# install backend packages
COPY poetry.toml poetry.toml
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN set -ex && poetry install --no-root

COPY . .

RUN yarn build
