In object oriented programming, two or more objects interact with each other. 
Objects are containers which contains state and behaviours. The state represents what object has  and behavior represents what object can do.

Example: 
Car class - Car has windows,doors, wiper,types - attributes

Car can move, stop - behaviour

In python, classes themself are objects unlike other programming language.
```
class Programmer:
    language = "python"
    version = 2.7

print("The type of class is object {}".format(type(Programmer)))
print(Programmer.language)
print(Programmer.__dict__)
print(getattr(Programmer,'language'))
print(getattr(Programmer,'operating system','N/A'))

#Adding class attribute at run time
setattr(Programmer,'operating system','Windows')
print(getattr(Programmer,'operating system','N/A'))
```
-------------------------------------------------------------------------------
Output of above program
-------------------------------------------------------------------------------
```
The type of class is object <class 'type'>
python
{'__module__': '__main__', 'language': 'python', 'version': 2.7, '__dict__': <attribute '__dict__' of 'Programmer' objects>, 
'__weakref__': <attribute '__weakref__' of 'Programmer' objects>, '__doc__': None}
python
N/A
Windows
```
```
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self._marks = None

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,marks):
        self._marks = marks

    def total(self):
        return sum(self.marks)

    def __eq__(self, other):
        return self.total() == other.total()

    def __add__(self,other):
        return self.total() + other.total()

    def __sub__(self, other):
        return self.total() - other.total()

    def __gt__(self, other):
        return self.total() > other.total()

    def __ge__(self, other):
        return self.total() >= other.total()

s1 = Student("john",23)
s2 = Student("doe",23)
s1.marks= [23,45,68]
print(s1.total())

s2.marks= [23,45,68]
print(s2.total())
if s1 == s2:
    print("scores match")
else:
    print("Scores does not match")
s3 = Student("alan",23)
s3.marks= [23,51,68]
print(s3.total())
if s3 == s2:
    print("scores match")
else:
    print("Scores does not match")

print(s1+s3)
print(s1>=s2)

output:
136
136
scores match
142
Scores does not match
278
True
```
