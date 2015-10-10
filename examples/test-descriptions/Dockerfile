FROM busybox:latest

LABEL io.hica.bind_pwd.test.guest='echo $(pwd)'
LABEL io.hica.bind_pwd.test.host='[ $(pwd) != "/" ]'
LABEL io.hica.bind_pwd.description='BINDING PWD'
LABEL io.hica.bind_pwd='1'

ENTRYPOINT ls
