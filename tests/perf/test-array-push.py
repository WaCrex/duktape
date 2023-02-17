def test():
    i = 0
    while i < 1e5:
        arr = []
        for _ in range(10):
            arr.extend(
                (
                    'foo',
                    'bar',
                    'foo',
                    'bar',
                    'foo',
                    'bar',
                    'foo',
                    'bar',
                    'foo',
                    'bar',
                )
            )
        i += 1

test()
