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

def params(paramDict):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for k, v in paramDict.items():
                print("%s: %s" % (k, v))
            return func(*args, **kwargs)
        return wrapper
    return decorator

def header():
    pass

def body(bodyDict):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for k, v in bodyDict.items():
                print("%s: %s" % (k, v))
            return func(*args, **kwargs)
        return wrapper
    return decorator

def response(responseDict):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for k, v in responseDict.items():
                print("%s: %s" % (k, v))
            return func(*args, **kwargs)
        return wrapper
    return decorator