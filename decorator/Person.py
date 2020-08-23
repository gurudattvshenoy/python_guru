import time
from functools import wraps
def log(func):

    @wraps(func)
    def inner(*args, **kwargs):
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
    print("Hi.. {}".format(name))
    return 100
print(greet("Gurudatt"))


class Person:
    ''' Person class '''

    def __init__(self, name, age):
        # _name and _age are instance variable and _ convention is used for private variables
        self._name = name
        self._age = age


    @property
    @log
    def name(self):
        ''' This returns person's name '''
        return self._name


    @name.setter
    @log
    def name(self, name):
        if len(self.name.strip()) > 1 and isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Name cannot be empty and must be of type str")


    @property
    @log
    def age(self):
        ''' This returns person's age '''
        return self._age


    @age.setter
    @log
    def age(self, age):
        if self.age > 0 and isinstance(age, int):
            self._age = age
        else:
            raise ValueError("Age must be postive value and must be of type int")

    @log
    def __repr__(self):
        return 'Person(name = {}, age = {})'.format(self.name, self.age)

    @staticmethod
    @log
    def is_adult(age):
        return age >= 18


p = Person("Guru", 34)
print(p.name)

# Raises/throws ValueError exception of setter
# p.name = 1
# print(p.name)
# p.age = "str"

p.age = 25
print("Is  {} adult? {}".format(p, p.is_adult(p.age)))
print("Person instance p __dict__ property {} ".format(p.__dict__))
print('Person class __dict__ property {}'.format(Person.__dict__))
