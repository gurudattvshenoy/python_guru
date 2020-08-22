import time
from functools import wraps
def log(func):

    @wraps(func)
    def inner(*args,**kwargs):
        print("Started executing {}()".format(func.__qualname__))
        start_time = time.perf_counter()
        ret = func(*args,**kwargs)
        print("Completed executing {}()".format(func.__qualname__))
        run_time = time.perf_counter()   - start_time  # 3
        time.sleep(2)
        print("The program returned result {}".format(ret))
        print(f"Finished {func.__name__!r}() in {run_time:4f} secs")
        return ret
    return inner

@log
def greet(name):
    return "Great day.. {}".format(name)
greet("Gurudatt")


class Person:
    def __init__(self,name):
        self.name = name
        
    @log
    def name(self):
        return self.age


Person("Gurudatt").name()
