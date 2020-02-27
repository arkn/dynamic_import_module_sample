#!/usr/bin/env python
import importlib
import json

f = open('config/test.json', 'r')
j = json.load(f)
print(j)

plugin_pkg_name = 'plugin.' + j['plugin']['pkg']

m = importlib.import_module(plugin_pkg_name)

m.sayhello()
