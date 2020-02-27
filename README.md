# dynamic_import_module_sample

## tree strcuture
```
$ tree
.
├── README.md
├── config
│   └── test.json
├── main.py
└── plugin
    └── func.py
```

## example result
```
$ ./main.py
{'key': {'name': 'test1', 'ver': '1.0.0'}, 'plugin': {'pkg': 'func1'}}
hey hello
{'key': {'name': 'test2', 'ver': '1.0.0'}, 'plugin': {'pkg': 'func2'}}
Buon giorno
```
