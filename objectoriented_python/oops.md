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
