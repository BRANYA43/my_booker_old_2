# Decorate for use class
def reiterate_func(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            func(self, arg, **kwargs)
    return wrapper
