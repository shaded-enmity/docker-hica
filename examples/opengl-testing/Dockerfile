FROM ubuntu:precise
MAINTAINER Jon Weisz <jon.weisz@gmail.com>

LABEL io.hica.xsocket_passthrough=1
LABEL io.hica.machine_id=1
LABEL io.hica.bind_pwd=1
LABEL io.hica.dri_passthrough=1
LABEL io.hica.introspect_runtime="glxinfo"
LABEL io.hica.introspect_runtime.whitelist="libGL.so:libX11.so:libxcb-dri2.so:libxcb.so:libati.*\.so:fglrx.*\.so"


RUN apt-get update && apt-get install -y mesa-utils

# Add a user so that UID 1000 exists. If the UID doesn't match, xauthentication is harder to deal with
RUN useradd docker
RUN echo "docker:docker" | chpasswd


ENTRYPOINT ["glxinfo"]
