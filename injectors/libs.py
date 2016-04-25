# vim: set fileencoding=utf-8
# Pavel Odvody <podvody@redhat.com>
#
# HICA - Host integrated container applications
#
# MIT License (C) 2015

import os, sys
from json import loads
from base.hica_base import *

library_path='/usr/lib64'

class LibraryInjector(HicaInjector):
  def _get_libs(self):
    return sorted(loads(self.labels.get_value('io.hica.libraries')))

  def get_description(self):
    return 'Bind mounts libraries {0} into the container'.format(', '.join(self._get_libs()))

  def get_config_key(self):
    return 'io.hica.libraries'

  def get_injected_args(self):
    return (('--libraries', HicaValueType.STRING, ''), ('--library-path', HicaValueType.PATH, '/usr/lib64'))

  def inject_config(self, config, from_args):
    """
    :param config:
    :type config: list
    :param from_args:
    :type from_args: dict
    """

    load_libs = self._get_libs()

    all_libs = {}
    found_libs = []
    
    for root, dirs, files in os.walk(library_path):
      for f in files:
        if not f.endswith('.so'):
          continue

        full_path = os.path.join(root, f)
        if '.' in f:
          name, ext = f.split('.', 1)
        else:
          name = f

        if name in all_libs:
          all_libs[name].append(full_path)
        else:
          all_libs[name] = [full_path]

    for lib in load_libs:
      if 'lib' + lib in all_libs:
        p = list(sorted(all_libs['lib' + lib], key=lambda x: len(x))).pop()
        v = '--volume={0}:{1}'.format(os.path.realpath(p), p)
        config.append(v)
      else:
        print('*** Unknown lib: {}'.format(lib))
        sys.exit(1)
