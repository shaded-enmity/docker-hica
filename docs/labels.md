Label Metadata Definition for HICA
----------------------------------

All labels live in common namespace `io.hica`, each set of labels with defined
values and name of command line parameter for supplying the value is versioned 
under `schema` versions. 

## Label Schema v0.3

| Label | Command line | Values | Default Value |
|-------|--------------|--------|---------------|
| io.hica.xsocket_passthrough | --xsocket-path, --x-display-num | *path*, *string* | `/tmp/.X11-unix`, `DISPLAY=:0` |
| io.hica.dri_passthrough | --dri-passthrough-path | *glob* | `/dev/dri/*` |
| io.hica.machine_id | --machine-id-path | *path* | `/etc/machine-id`|
| io.hica.cuda | --cuda-device, --cuda-device-ctl, --cuda-device-uvm | *path*, *path*, *path* | `/dev/nvidia0`, `/dev/nvidiactl`, `/dev/nvidia-uvm` |
| io.hica.sound_device | --sound-device | *glob* | `/dev/snd*` |
| io.hica.pulse | --pulse | *path* | `/run/user/$UID/pulse/` |
| io.hica.bind_home | --home-path | *path* | `$HOME` |
| io.hica.bind_pwd | *none* | *none* | `$PWD` |
| io.hica.bind_users_groups | --users-path, --groups-path | *path*, *path* | `/etc/passwd`, `/etc/group` |
| io.hica.bind_localtime | --time-path | *path* | `/etc/localtime` |
| io.hica.env_passthrough | --env | `none`, `full` | `full` |
| io.hica.kvm_passthrough | --kvm-device | *path* | `/dev/kvm` |

#### Complementary labels

| Label | Command line | Values | Default Value |
|-------|--------------|--------|---------------|
| io.hica.introspect_runtime=[] | --introspect-runtime | *path* | `none` |
| io.hica.library_whitelist=[] | --library-whitelist | *glob* | `none` |

---

Note that `introspect_runtime` and `library_whitelist` are complementary labels, let's see an example usage:

```
LABEL io.hica.introspect_runtime="glxinfo"
LABEL io.hica.library_whitelist="libGL.so:libX11.so:libxcb-dri2.so:libxcb.so"
```

What is hapenning? If you ever tried to work with `OpenGL`/`OpenCL` or just `DRI` in general in a container / virtual environment, you've had to figure out the hard way that if there's even slightest disparity between particular driver versions betweem host and container that it _just doesn't work_.
So the `introspect_runtime` label executes the `glxinfo` utility on host, while `strace`'ing it for loaded `DSO`'s. 
The resulting `DSO`'s are then compared with the contents of the `library_whitelist` label and only matching libraries are being passed.

Please note that *all* versions (`SOnames`) of the specified shared object will be linked.

### Testing that injectors work

Image authors who target a wide variety of different host systems may want to be able to verify that the injectors work correctly before doing anything else. For that purpose, there's an option to specify in-container test binary for the given injector. Building on the reverse DNS notation, simply append `.test.host` or `.test.guest` to the label definition and specify the binary to execute:

```
LABEL io.hica.kvm_passthrough.test.guest='/opt/tests/kvm'
```

Note that **ALL** tests that are specified have to succeed during the test case run.

### Adding human-readable description to injectors

Some injectors may require additional description text besides the generic summary found directly in code.
For that purpose you can use the `.description` namespace for the given label, which might be especially valuable in the context of labels that accept additional parameters (`introspect_runtime`, `library_whitelist`).

```
LABEL io.hica.introspect_runtime="glxinfo"
LABEL io.hica.introspect_runtime.description="DRI/OpenGL Runtime Dependencies"
```

### Summary of supplementary label namespaces

| Value | Description |
|-------|-------------|
| *.test.host | Test command executed on host |
| *.test.guest | Test command executed on guest |
| *.description | Human readable description of the injector |
