SELinux support
---------------

By default, all containers run in unconfined domain. This is the *de facto* standard in the desktop world.
While running in the unconfined domain, the process is not subject to technically any SELinux restrictions, besides booleans.
In this case the system relies on Discretionary Access Control (DAC) mechanism to enforce isolation boundaries therefore it's crucial to
run all containers as non-root, except for the cases of system tools containers.
If you know that there exists a policy for the application and that it works, you can specify `--selinux-label=my_app_t` to label
the process with the given type.
The reason for not running as the default `svirt_lxc_net_t` is that that type is allowed to access only files labeled as `svirt_sandbox_file_t`, and as a result, all
files that are bind mounted into the container with the `:z/:Z` mount option will be relabeled to that type, which can be disasterous in case of system files.

#### Running with custom label

```
$ ./docker-hica --selinux-label=firefox_t firefox:1.0
```
