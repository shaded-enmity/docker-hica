# vim: set fileencoding=utf-8
# Pavel Odvody <podvody@redhat.com>
#
# HICA - Host integrated container applications
#
# MIT License (C) 2015

import os
from base.hica_base import *

class XSocketInjector(HicaInjector):
  def get_description(self):
    return 'Bind mounts XSocket into the container'

  def get_config_key(self):
    return 'io.hica.xsocket_passthrough'

  def get_injected_args(self):
    return (('--xsocket-path', HicaValueType.PATH, '/tmp/.X11-unix'), 
        ('--x-display-num', HicaValueType.STRING, 'DISPLAY=' + os.getenv('DISPLAY')))
