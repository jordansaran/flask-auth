FROM python:3.12-slim
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOMEBREW_INSTALL_FROM_API 1
RUN apt update -y && apt install -y build-essential libpq-dev wget procps curl file git mlocate

RUN apt update -y  &&  \
    apt upgrade -y &&  \
    apt-get update &&  \
    pip install --upgrade pip setuptools wheel

COPY ./requirements.txt /usr/src/app/requirements.txt

COPY ./.env.example /usr/src/app/.env

RUN pip install -r requirements.txt

COPY . /usr/src/app/

RUN chmod -R 777 /usr/src/app/

ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]

EXPOSE 8000