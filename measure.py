import timeit

def measure(f):
    def wrapper(*args, **kw):
        s = timeit.default_timer()
        output = f(*args, **kw)
        e = timeit.default_timer()
        us = 1e-6
        print(f'{f.__name__} execution time: {(e-s)/us:.4}us')
        return output
    return wrapper