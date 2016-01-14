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

LABEL io.hica.command_aliases='{"create-key": {"cmd": "-G -p {0}.pub -s {0}.sec", "synopsis": "keyfile"}, \
                                "sign": {"cmd": "-S -x {0} -s {1} -m {2}", "synopsis": "sigfile privkey file"}, \
                                "verify": {"cmd": "-V -x {0} -p {1} -m {2}", "synopsis": "sigfile pubkey file"}}'
ENTRYPOINT ["signify"]
