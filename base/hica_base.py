# vim: set fileencoding=utf-8
# Pavel Odvody <podvody@redhat.com>
#
# HICA - Host integrated container applications
#
# MIT License (C) 2015

import glob, os, sys, re

class HicaValueType(object):
  (NONE, PATH, DEVICE, GLOB, STRING, FULLENV) = [0] + [1 << x for x in range(5)]

class HicaInjector(object):
  def get_description(self):
    return None

  def get_config_key(self):
    return None

  def get_injected_args(self):
    return None

  def inject_value_type(self, value, config):
    typ, val = value
    if typ & HicaValueType.PATH:
      if val and val != "none":
        if typ & HicaValueType.GLOB:
          for v in glob.glob(val):
            config.append("--volume")
            config.append("{0}:{0}".format(v))
        else:
          config.append("--volume")
          config.append("{0}:{0}".format(val))
    elif typ & HicaValueType.DEVICE:
      if val and val != "none":
        if typ & HicaValueType.GLOB:
          for v in glob.glob(val):
            config.append("--device")
            config.append("{0}:{0}".format(v))
        else:
          config.append("--device")
          config.append("{0}:{0}".format(val))
    elif typ == HicaValueType.STRING:
      config.append("-e")
      config.append(val)
    elif typ == HicaValueType.FULLENV:
      for k, v in val.iteritems():
        config.append("-e")
        config.append("{0}={1}".format(k, v))

  def inject_config(self, config, from_args):
    for cv in from_args:
      self.inject_value_type(cv, config)

class HicaLabelStore(object):
  PREFIX = 'io.hica'
  def __init__(self, labels):
    self.items = labels

  def query(self, ns, selector='*'):
    """ Query the label store for labels

    :param ns: Label namespace (`bind_pwd` for example)
    :type ns: str
    :param selector: Target selector (`test` or `test.guest` for example)
    :type selector: str
    
    """
    q, r = HicaLabelStore.PREFIX + '.' + ns, []
    for (key, value) in self.items:
      if key.startswith(q) and key != q:
        sub = key[len(q):]
        m = re.match('.' + selector, sub)
        if m:
          r.append((key, value))
    return r

  def query_full(self, label, selector='*'):
    """ Same as `query` but strips all the prefixes """
    return self.query(label.rsplit('.', 1)[1], selector)

class HicaConfiguration(object):
  def __init__(self):
    pass

class HicaDriverBase(object):
  def __init__(self):
    pass

  def launch_container(self, config):
    pass

def main():
  pass

if __name__ == "main":
  main()
