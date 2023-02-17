import math
import random

def test():
    print('build')
    tmp1 = [chr(random.randint(0, 127)) for _ in xrange(1024)]
    tmp1 = ''.join(tmp1)
    tmp2 = [tmp1 for _ in xrange(1024)]
    tmp2 = ''.join(tmp2)
    tmp2 = tmp2.encode('base64')

    tmp3 = [tmp2[i:i+77] for i in range(0, len(tmp2), 77)]
    tmp2 = '\n'.join(tmp3) + '\n'

    print(len(tmp2))
    print('run')
    for _ in xrange(2000):
        res = tmp2.decode('base64')

test()
