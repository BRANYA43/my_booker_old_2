# Decorate
def reiterate_func(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            func(arg, **kwargs)
    return wrapper
