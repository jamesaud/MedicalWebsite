FROM mysql:5.7
MAINTAINER Wodby <admin@wodby.com>


ENV BASH_SOURCE /bin/bash

RUN mkdir -p /var/run/mysqld
RUN chown 100:101 /var/run/mysqld

#RUN mkdir /docker-entrypoint-initdb.d
COPY my.cnf /etc/mysql/my.cnf
COPY docker-entrypoint.sh /usr/local/bin/

WORKDIR /var/lib/mysql
VOLUME /var/lib/mysql

EXPOSE 3306

#ENTRYPOINT ["docker-entrypoint.sh"]
#CMD ["mysqld"]
