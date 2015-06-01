FROM fedora
MAINTAINER langdon <langdon@fedoraproject.org>
RUN yum clean all && yum -y update
RUN yum -y install python python-pip make gcc krb5-devel python-devel python-setuptools
RUN yum -y install python-setuptools python-kerberos python-nitrate python-dateutil python-urllib2_kerberos
RUN yum clean all

COPY . /opt/sniprd
WORKDIR /opt/sniprd
RUN python setup.py install
#RUN ln -s /user-home/.sniprd /root/.sniprd
RUN ln -s /sniprd.conf /root/.sniprd

VOLUME /sniprd.conf

LABEL RUN docker run --privileged --rm -it -v $(HOME)/.sniprd:/sniprd.conf $(USERNAME)/sniprd 

ENTRYPOINT ["/usr/bin/snip"]
