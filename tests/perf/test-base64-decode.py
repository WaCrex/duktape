import math
import random

def test():
    print('build')
    tmp1 = [chr(random.randint(0, 127)) for _ in xrange(1024)]
    tmp1 = ''.join(tmp1)
    tmp2 = [tmp1 for _ in xrange(1024)]
    tmp2 = ''.join(tmp2)
    tmp2 = tmp2.encode('base64')

    print(len(tmp2))
    print('run')
    for _ in xrange(2000):
        res = tmp2.decode('base64')

test()
