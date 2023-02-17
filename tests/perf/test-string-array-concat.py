def test():
    for _ in xrange(int(5e3)):
        t = ['x' for _ in xrange(int(1e4))]
        t = ''.join(t)

test()
