FROM fedora:22
MAINTAINER Pavel Odvody <podvody@redhat.com>

LABEL io.hica.xsocket_passthrough=1
LABEL io.hica.dri_passthrough=1
LABEL io.hica.introspect_runtime="glxinfo"
LABEL io.hica.introspect_runtime.whitelist="libGL.so:libX11.so:libxcb-dri2.so:libxcb.so:libati.*\.so:fglrx.*\.so:libnvidia*"

RUN dnf install -y glx-utils
RUN useradd docker

ENTRYPOINT ["glxinfo"]
