from functools import wraps

def timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

@timer
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)