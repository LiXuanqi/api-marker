import functools


def api(method, path, desc, params={}, body={}, response={}):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("method=%s" % method)
            print("path=%s" % path)
            print("desc=%s" % desc)
            # - params
            for k, v in params.items():
                print("%s: %s" % (k, v))
            # - body
            for k, v in body.items():
                print("%s: %s" % (k, v))
            # - response
            for k, v in response.items():
                print("%s: %s" % (k, v))
            return func(*args, **kwargs)
        return wrapper
    return decorator
