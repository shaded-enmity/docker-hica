HICA (Host Integrated Container Applications) v0.5.1
----------------------------------------------------
[hɑɪkː]

The goal of this project is to define a set of image label metadata 
and launcher tooling that understands said metadata to provide for
smooth experience running containerized applications with tight
integration with the host operating system.

### Installation

```
pip install docker-hica
```

### Docs

Versioned specification of all labels can be found in [docs/labels.md](docs/labels.md)

Guidelines for Dockerfiles can be found in [docs/dockerfile-guidelines.md](docs/dockerfile-guidelines.md)

SELinux usage is documented in [docs/selinux.md](docs/selinux.md)

### Examples

Examples directory currently contains several example Dockerfiles:
 * `jq`
 * `firefox-testing`
 * `signify`
 * `opengl-testing`
 * `test-description`

Please refer to `README.md` in each particular subdirectory for more information.
The straightforward way is to simply:
```bash
$ cd examples/example
$ docker build -t example .
$ docker-hica example
```

### Advanced usage

Let's overview the basic stuff:

```bash
$ docker-hica --help
usage: docker-hica [-h] [--show-args] [--test-injectors] [--verbose] [--yes]
                   [--selinux-label SELINUX_LABEL] [--user USER]
                   hica_app_name ...

positional arguments:
  hica_app_name
  named_action

optional arguments:
  -h, --help            show this help message and exit
  --show-args           show possible arguments for the specified
                        "hica_app_name"
  --test-injectors      executes injector tests for specified "hica_app_name"
  --verbose             print additional information
  --yes                 bypass the capability review check
  --selinux-label SELINUX_LABEL
                        provide a confinement context
  --user USER           user:group to run as (1000:1000)
```

The `--show-args` flag allows for displaying configurable parameters for image injectors, so
to see what parameters can be passed to the `examples/firefox` image, execute:
```bash
$ docker-hica --show-args firefox:1.0
usage: docker-hica [-h] [--show-args] [--verbose] [--yes]
                   [--machine-id-path MACHINE_ID_PATH]
                   [--xsocket-path XSOCKET_PATH]
                   [--x-display-num X_DISPLAY_NUM]
                   hica_app_name ...
```

When `--verbose` is specified, the Docker command is also printed out during execution:
```bash
$ docker-hica --verbose firefox:1.0
The container requests the following capabilities: 
 - Bind mounts current working directory (/Repos/docker-hica) into the container
 - Bind mounts machine-id into the container
 - Bind mounts XSocket into the container
Proceed? [y/Y/n]: y
Executing: docker run -i -u 1000:1000 --volume /Repos/docker-hica:/Repos/docker-hica -w /Repos/docker-hica --volume /etc/machine-id:/etc/machine-id --volume /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=:0 firefox:1.0
```

And finally the `--yes` flag allows for skipping the initial prompt for confirmation as seen on the example above.
This option is dangerous, future versions will treat 'Y' in the prompt response as 'Yes and remmber', so that
the initial capability request is reviewed at least once.
