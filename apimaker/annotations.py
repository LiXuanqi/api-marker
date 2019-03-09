import functools


def api(method, path, desc):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("method=%s" % method)
            print("path=%s" % path)
            print("desc=%s" % desc)
            return func(*args, **kwargs)
        return wrapper
    return decorator
