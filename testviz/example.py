from viztracer import VizTracer


def inner(i: int) -> bool:
    if i <= 0:
        return False
    if not i:
        return True
    return inner(i - 1)


def outer():
    a, b = 1, 2
    inner(a)
    inner(b)
    print('done')


outer()
