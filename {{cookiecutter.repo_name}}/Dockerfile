# Base image.
FROM archlinux/base

# Create code folder.
RUN mkdir /code

# Set working dir.
WORKDIR /code

# Add python requirements file.
ADD requirements.txt /code/

# Install required programs.
RUN set -xe; \
    pacman -Sy --noconfirm \
    python \
    python-pip \
    # gettext \
    nginx \
    vim \
    gcc-multilib

RUN pacman -S -c -c  --noconfirm

RUN pip install --no-cache-dir  -r requirements.txt

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /code/conf/nginx-app.conf /etc/nginx/sites-enabled/

# Add source code.
ADD . /code/

# Run script file.
CMD ./run.sh