MAINTAINER Humphrey Butau
FROM hamub/django:v2
# Let us copy our requirements file so that we can install our python dependencies.
ADD requirements.txt /requirements.txt

RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
            postgresql-dev \
            libxslt-dev \
            libgcc \
            zlib-dev \
            jpeg-dev \
            gcc \
    && pip install -U pip \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pip install --no-cache-dir -r requirements.txt " \ 
    # && apk del .build-deps
# Set the project directory for the source code to:  /home/django
WORKDIR /home/django/
# Copy our source code to the working directory
ADD . /home/django
# Run migrations, collectstatic, start uwsgi .... e.t.c
CMD ["/home/django/run-prod.sh"]
