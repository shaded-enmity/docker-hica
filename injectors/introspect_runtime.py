# vim: set fileencoding=utf-8
# Pavel Odvody <podvody@redhat.com>
#
# HICA - Host integrated container applications
#
# MIT License (C) 2015

import os
from base.hica_base import *
import subprocess
_container_lib_location = '/external_libs'

class IntrospectRuntimeInjector(HicaInjector):

  def get_description(self):
    return 'Traces a binary ({0}) which makes a white list of libraries to be mounted into the container'.format(self.labels.get_value('io.hica.introspect_runtime'))

  def get_config_key(self):
    return 'io.hica.introspect_runtime'

  def get_injected_args(self):
    return (('--introspect-runtime', HicaValueType.PATH, ''),
             ('--introspect-runtime-whitelist', HicaValueType.STRING, ''))

  def _get_runtime(self):
    return self.labels.get_value('io.hica.introspect_runtime')

  def _get_whitelist(self):
    return self.labels.get_value('io.hica.introspect_runtime.whitelist').split(':')

  def _run_introspection(self, runtime='', whitelist=[], verbose=False):
    """ Figure out which objects are opened by a test binary and are matched by the white list. 

    :param runtime: The binary to run. 
    :type runtime: str
    :param whitelist: A list of regular expressions describing acceptable library names
    :type whitelist: [str]    
    """
    found_objects = set()
    try:
      # Retrieve list of successfully opened objects
      strace = subprocess.Popen(['strace', runtime], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
      (_, stderr) = strace.communicate()
      opened_objects = set()
      for line in stderr.split('\n'):
        if 'open' in line and 'ENOENT' not in line:
          start = line.index('"')
          end = line.index('"', start + 1)
          opened_objects.add(line[start + 1:end])

      # filter opened objects through white list.
      for obj in opened_objects:
        for wl in whitelist:
          m = re.match('.*' + wl + '[\..*]?', obj)
          if m:
            found_objects.add(obj)
            if verbose:
              print('Found whitelisted {} at path {}'.format(wl, obj))
            continue
    except Exception as e:
      print e

    return found_objects

  def __get_container_path(self, host_path):
    """ A simple helper function to determine the path of a host library
    inside the container

    :param host_path: The path of the library on the host
    :type host_path: str
    """
    libname = os.path.split(host_path)[1]
    return os.path.join(_container_lib_location, libname)

  def __remove_duplicates(self, library):
    libset = set()
    unique_libs = []
    for lib in library:
      unique_libs.append(lib)

  def inject_config(self, config, from_args):
    """
    :param config:
    :type config: list
    :param from_args:
    :type from_args: dict
    """
    # First get required values from labelStore
    runtime = self._get_runtime()
    whitelist = self._get_whitelist()
    #Run introspection on the libraries to retrieve list of libraries to link
    found_libraries = self._run_introspection(runtime, whitelist, verbose=True)
    container_path_set=set()
    for library in found_libraries:

      #disallow duplicate library targets
      cpath = self.__get_container_path(library)
      if cpath in container_path_set:
        continue
      container_path_set.add(cpath)

      config.append('--volume={0}:{1}'.format(library, cpath))
    
    config.extend(['-e', 'LD_LIBRARY_PATH={0}'.format(_container_lib_location)])
    config.extend(['-e', 'LIBGL_DRIVERS_PATH={0}'.format(_container_lib_location)])
