def reiterate_func_with_one_arg(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            func(self, arg, **kwargs)
    return wrapper


def reiterate_func_with_two_args(func):
    def wrapper(self, *args, **kwargs):
        for i in range(0, len(args), 2):
            func(self, args[i], args[i+1], **kwargs)
    return wrapper


def reiterate_func_with_three_args(func):
    def wrapper(self, *args, **kwargs):
        for i in range(0, len(args), 3):
            func(self, args[i], args[i+1], args[i+2], *kwargs)
    return wrapper


def reiterate_get_func_with_one_arg(func):
    def wrapper(self, *args, **kwargs):
        if len(args) == 1:
            return func(self, args[0], **kwargs)
        else:
            ret = []
            for arg in args:
                ret.append(func(self, arg, **kwargs))
            return tuple(ret)
    return wrapper


def reiterate_get_func_with_two_args(func):
    def wrapper(self, *args, **kwargs):
        if len(args) == 2:
            return func(self, args[0], args[1], **kwargs)
        else:
            ret = []
            for i in range(0, len(args), 2):
                ret.append(func(self, args[i], args[i + 1], **kwargs))
            return tuple(ret)
    return wrapper


def is_object_select(func):
    def wrapper(self, *args, **kwargs):
        if self.model.selected_object is not None:
            func(self, *args, **kwargs)
    return wrapper
