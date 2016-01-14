FROM fedora:23
MAINTAINER Pavel Odvody <podvody@redhat.com>

LABEL io.hica.bind_pwd=1
LABEL io.hica.bind_home=1
LABEL io.hica.tty=1

ENV BUILD_PKGS='libbsd-devel make gcc findutils git'

RUN dnf install -y libbsd ${BUILD_PKGS}\
 && (git clone https://github.com/aperezdc/signify && cd signify\
 && make && make install && rm -rf /signify)\
 && dnf remove -y ${BUILD_PKGS} && rm -rf /var/cache/dnf/

ENTRYPOINT ["signify"]
