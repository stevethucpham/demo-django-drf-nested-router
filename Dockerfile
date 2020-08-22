FROM python:3.8-alpine
LABEL maintainer="Thuc Pham"

# It doesn't allow python to buffer the output in docker container.
# Avoid some complications with docker image
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# No cache will reduce the size of your image
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
     gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Create a dir app for the docker image
RUN mkdir /app
# Start with this dir
WORKDIR /app
# Copy into our docker image
COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user -R /vol/
RUN chown -R 755 /vol/web
USER user


