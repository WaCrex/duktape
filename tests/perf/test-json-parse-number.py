import json
import random

def test():
    arr = [random.random() * 1e9 for _ in xrange(10000)]
    jsondata = json.dumps(arr)
    print(len(jsondata))
    #print(jsondata)

    for _ in xrange(100):
        ign = json.loads(jsondata)

test()
