signify docker-hica example
---------------------------

An example Dockerfile that utilizes the `io.hica.bind_pwd` and `io.hica.bind_home` labels to bind current working 
directory and home directory, respectively, into the container. Our image contains Linux port of the BSD signify
tool for cozy signing using ECC cryptography.

```bash
$ cd examples/signify
$ docker build -t signify .
$ mkdir -p ~/.signify_keyes/
$ cd ../..
# generate keys in home directory
$ docker-hica signify -- -G -p ~/.signify_keys/hica_test.pub -s ~/.signify_keys/hica_test.sec
# sign 'docker-hica' executable
$ docker-hica signify -- -S -x docker-hica.sig -s ~/.signify_keys/hica_test.sec -m docker-hica
# verify signatures
$ docker-hica signify -- -V -x docker-hica.sig -p ~/.signify_keys/hica_test.pub -m docker-hica
Signature Verified
```

## Command aliases usage
This image ships with 3 aliases for the above scary commands:
```bash
$ docker-hica signify create-key mykey
secret
secret
$ docker-hica signify sign file.sig mykey.sec file
secret
$ docker-hica signify verify file.sig mykey.pub file
Signature Verified
```

To check the arguments you can also do:
```bash
$ docker-hica signify sign help
sign synopsis:
 sigfile privkey file
```
