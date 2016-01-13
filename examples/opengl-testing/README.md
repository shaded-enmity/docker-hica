opengl-testing
--------------

This HICA image exercises running containerized OpenGL applications via dynamic runtime introspection.
The `glxinfo` utility is used to dump a complete list of OpenGL capabilities.

```
$ docker build -t opengl .
$ cd ../..
$ ./docker-hica --verbose opengl
Found whitelisted libxcb.so at path /usr/lib64/libxcb.so.1.1.0
Found whitelisted libGL.so at path /usr/lib64/libGL.so.355.11
Found whitelisted libnvidia* at path /usr/lib64/libnvidia-glcore.so.355.11
Found whitelisted libX11.so at path /lib64/libX11.so.6
Found whitelisted libX11.so at path /usr/lib64/libX11.so.6.3.0
Found whitelisted libxcb.so at path /lib64/libxcb.so.1
Found whitelisted libnvidia* at path /lib64/libnvidia-glcore.so.355.11
Found whitelisted libnvidia* at path /lib64/tls/libnvidia-tls.so.355.11
Found whitelisted libnvidia* at path /usr/lib64/tls/libnvidia-tls.so.355.11
Found whitelisted libGL.so at path /lib64/libGL.so.1
The container requests the following capabilities:
 - Bind mounts XSocket into the container
 - Traces a binary (glxinfo) which makes a white list of libraries to be mounted into the container
 - Bind mounts direct rendering interface devices (DRI) into the container
Proceed? [y/Y/n]: y
Executing: docker run -i -u 1000:1000 --volume /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=:1 --volume=/usr/lib64/libxcb.so.1.1.0:/external_libs/libxcb.so.1.1.0 --volume=/lib64/libX11.so.6:/external_libs/libX11.so.6 --volume=/usr/lib64/tls/libnvidia-tls.so.355.11:/external_libs/libnvidia-tls.so.355.11 --volume=/lib64/libGL.so.1:/external_libs/libGL.so.1 --volume=/usr/lib64/libX11.so.6.3.0:/external_libs/libX11.so.6.3.0 --volume=/usr/lib64/libGL.so.355.11:/external_libs/libGL.so.355.11 --volume=/usr/lib64/libnvidia-glcore.so.355.11:/external_libs/libnvidia-glcore.so.355.11 --volume=/lib64/libxcb.so.1:/external_libs/libxcb.so.1 -e LD_LIBRARY_PATH=/external_libs -e LIBGL_DRIVERS_PATH=/external_libs --device /dev/dri/card0:/dev/dri/card0 --device /dev/nvidia0:/dev/nvidia0 --device /dev/nvidiactl:/dev/nvidiactl opengl
==>
(glxinfo output snipped)
```
