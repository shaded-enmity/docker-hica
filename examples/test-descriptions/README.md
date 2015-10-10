tests-descriptions
------------------

Test of guest/host test labels and also injector description label.
The test image has tests for the `bind_pwd` injector as well as additional description message

```
$ docker build -t tests-descriptions .
$ cd ../..
$ ./docker-hica --test-injectors tests-descriptions
/
[(u'io.hica.bind_pwd', u'echo $(pwd)')]
[(u'io.hica.bind_pwd', u'[ $(pwd) != "/" ]')]
$ ./docker-hica tests-descriptions
The container requests the following capabilities:
 - BINDING PWD
 - Bind mounts current working directory (/Repos/docker-hica) into the container
Proceed? [y/Y/n]: n
*** Operation aborted!
```
