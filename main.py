#!/usr/bin/env python
import os
import importlib
import json

for filename in os.listdir('config/.'):
  f = open('config/' + filename, 'r')
  j = json.load(f)
  print(j)
  
  plugin_pkg_name = 'plugin.' + j['plugin']['pkg']

  m = importlib.import_module(plugin_pkg_name)

  m.sayhello()
