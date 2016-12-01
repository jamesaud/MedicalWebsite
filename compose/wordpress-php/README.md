[![Docker Stars](https://img.shields.io/docker/stars/evild/alpine-wordpress.svg?style=flat-square)](https://hub.docker.com/r/evild/alpine-wordpress/)
[![Docker Pulls](https://img.shields.io/docker/pulls/evild/alpine-wordpress.svg?style=flat-square)](https://hub.docker.com/r/evild/alpine-wordpress/)
[![](https://images.microbadger.com/badges/image/evild/alpine-wordpress.svg)](https://microbadger.com/images/evild/alpine-wordpress)

# Alpine Wordpress

This image is based on [evild/alpine-php](https://hub.docker.com/r/evild/alpine-php/)

## Version

- `latest` [(Dockerfile)](https://github.com/Evild67/docker-alpine-wordpress/blob/master/Dockerfile)
- `4.6.1` [(Dockerfile)](https://github.com/Evild67/docker-alpine-wordpress/blob/b0fbdacc9965793cf20e3c6bfd9e10d6683313aa/Dockerfile)
- `4.6` [(Dockerfile)](https://github.com/Evild67/docker-alpine-wordpress/blob/a6581d3f764d3d10dfe863cbf66c3144f1e42672/Dockerfile)
- `4.5.4` [(Dockerfile)](https://github.com/Evild67/docker-alpine-wordpress/blob/43300ea22cdac08ecf738ee2619e81709adb9c51/Dockerfile)
- `4.5.3` [(Dockerfile)](https://github.com/Evild67/docker-alpine-wordpress/blob/a1ddef9ad8000d328671ed366e1c7c34246fdbdd/Dockerfile)
- `4.5.2` [(Dockerfile)](https://github.com/Evild67/docker-alpine-wordpress/blob/3ca44832bc8d1f30222665b1a00806461b10b851/Dockerfile)


## What is WordPress?
WordPress is a free and open source blogging tool and a content management system (CMS) based on PHP and MySQL, which runs on a web hosting service. Features include a plugin architecture and a template system. WordPress is used by more than 22.0% of the top 10 million websites as of August 2013. WordPress is the most popular blogging system in use on the Web, at more than 60 million websites. The most popular languages used are English, Spanish and Bahasa Indonesia.


## Installation
Automated builds of the image are available on Dockerhub and is the recommended method of installation.
```
docker pull evild/alpine-wordpress:4.5.3
```
You can also pull the latest tag which is built from the repository HEAD
```
docker pull evild/alpine-wordpress:latest
```
Alternatively you can build the image locally.
```
docker build -t evild/alpine-wordpress github.com/evild67/alpine-wordpress
```

## Quick Start

You can manually launch the Wordpress container and the supporting Nginx and Database containers.

MariaDB :
```
docker run -t mariadb -e MYSQL_ROOT_PASSWORD=password --link mariadb mariadb:latest
```
Wordpress :
```
docker run -t wordpress -e WORDPRESS_DB_HOST=mariadb -e WORDPRESS_PASSWORD=password --link mariadb evild/alpine-wordpress
```

Database & Wordpress containers are running. You can now link Wordpress to a nginx server.

## Available Configuration Parameters

Please refer the docker run command options for the --env-file flag where you can specify all required environment variables in a single file. This will save you from writing a potentially long docker run command. Alternatively you can use docker-compose.

Below is the complete list of available options that can be used to customize your WordPress installation.
* **WORDPRESS_DEBUG**: Set this to true to enable debugging.
* **WORDPRESS_DB_HOST** (REQUIRED): The hostname of the database server.
* **WORDPRESS_DB_USER**: The database database user. Defaults to `root`
* **WORDPRESS_DB_PASSWORD** (REQUIRED): The database database password.
* **WORDPRESS_DB_NAME**: The database database name. Defaults to to `wordpress`
* **WORDPRESS_AUTH_KEY**: Defaults to unique random SHA1s
* **WORDPRESS_SECURE_AUTH_KEY**: Defaults to unique random SHA1s
* **WORDPRESS_LOGGED_IN_KEY**: Defaults to unique random SHA1s
* **WORDPRESS_NONCE_KEY**: Defaults to unique random SHA1s
* **WORDPRESS_AUTH_SALT**: Defaults to unique random SHA1s
* **WORDPRESS_SECURE_AUTH_SALT**: Defaults to unique random SHA1s
* **WORDPRESS_WORDPRESS_LOGGED_IN_SALT**: Defaults to unique random SHA1s
* **WORDPRESS_NONCE_SALT**: Defaults to unique random SHA1s
