import functools
class Helper():
    @staticmethod
    def validateNumberInput(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            counter = 0
            containStringInput = False
            for item in args:
                if counter >= 1:
                    if type(item) not in (float,int):
                        print(type(item))
                        containStringInput = True
                        break
                counter += 1
            if containStringInput:
                raise ValueError("Input is not int or float")
            else:
                return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def validateListInput(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            containListInput = any([type(item) in (list,tuple) for item in args[1:len(args)]])
            for item in args[1:len(args)]:
                if type(item) in (list,tuple):
                    if len(item) == 0:
                        raise ValueError("list cannot be empty")
                    if any([type(num) not in (int, float) for num in item]):
                        raise ValueError("Number in the list not int or float")
            if not containListInput:
                raise ValueError("Parameter does not have list input")
            else:
                return func(*args, **kwargs)
        return wrapper




