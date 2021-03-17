FROM httpd:2.4.46

COPY httpd.conf /usr/local/apache2/conf/httpd.conf

ENV MYAPP_HOME /usr/local/apache2/htdocs
WORKDIR $MYAPP_HOME
COPY index.html .
EXPOSE 80
