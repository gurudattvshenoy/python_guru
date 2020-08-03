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
