def exec_time(func):
    from functools import wraps
    @wraps(func)
    def inner(*args,**kwargs):
        import time
        start_time = time.perf_counter()
        print("Executing... {}()".format(func.__name__))
        returnval = func(*args, **kwargs)
        print("Done executing...{}()".format(func.__name__))
        print(time.perf_counter() - start_time)
        return returnval
    return inner
@exec_time
def greet(name):
    import time
    time.sleep(3)
    print("Hello")



greet("guru")
