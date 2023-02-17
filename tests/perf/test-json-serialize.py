import json

def build():
    return {
        'key1': 'foo',
        'key2': 'bar',
        'key3': 'quux',
        'key4': 'baz',
        'key5': 'quuux',
        'key6': ['foo', 'bar', 'quux', 'baz', 'quuux'],
        'key7': [None, None, True, 123.456, 1e200, {}, {}, {}],
    }

def test():
    obj = build()
    i = 0
    while i < 1e5:
        ignore = json.dumps(obj)
        i += 1

test()
