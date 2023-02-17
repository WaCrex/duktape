import math
import random

def test():
    print('build')
    tmp1 = [chr(int(math.floor(random.random() * 256))) for _ in xrange(1024)]
    tmp1 = ''.join(tmp1)
    tmp2 = [tmp1 for _ in xrange(1024)]
    tmp2 = ''.join(tmp2)

    print(len(tmp2))
    print('run')
    for _ in xrange(5000):
        res = tmp2.encode('hex')

test()
