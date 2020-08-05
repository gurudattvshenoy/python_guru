# Dictionary

A dictionary consists of a collection of key-value pairs. Keys has to be hashable and values can be any python object.
Hashable objects are string,function,tuple,int, float, complex, binary, Decimal, Fraction. lists,sets,dictionaries are never hashable.
In otherwords, immutable data types are hashable whereas mutable data types are not.



**Creating Dictionary**

Created using comma-separated list of key-value pairs in curly braces ({}) and colon (:) separates  key and values.
Example:
```
1. sample_dict = {  key1: value1, 
                    key2: value2, 
                    key3: value3 
                 }
2. dict_obj ={ 'friends': ['John', 'alex', 36], 
                    (0, 0): 'origin', 
                    'mul': lambda x: x ** 2, 
                    'eric': {'name': 'Hawkes ', 'age': 56} 
    }
 3. Type of dictionary:
 >>> type(employee_guru)
     <class 'dict'>

```


**Initializing dictionary**

**1. Dictionary Comprehension:**
```
   squares_numbers = {
      str(i): i*i for i in range(1,10)
   }
   print(squares_numbers)
   
   Output:{'1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}
```

**2. Dictionary Comprehension:**
```
fromkeys takes iterable as first argument and second argument is default value to the keys.

d = dict.fromkeys(['a', (0,0), 100], 'N/A')

for (key,val) in d.items():
    print("{} - {}".format(key,val))

output:
a - N/A
(0, 0) - N/A
100 - N/A

```
d[key] = value 
creates key if it does not exist already and assigned the value
d[key] = as an expression, this returns the value for specified key 
      if key is not present then it throws KeyError exception 

d.get(key) - returns value if key is found, None if key is not found
d.get(key, default) - returns value if key is found, default if key is not found
membership testingkey in d - True if key is in d, False if it is not
number of items in dictionarylen(d)
d.clear()
del d[key] à removes element with that key from d à exception KeyError if key is not in d
d.pop(key) à removes element with that key from d à and returns the corresponding value à returns default is key was not found à exception KeyError if key is not in d
d.pop(key, default)

def insert_if_not_present(d, key, value): if key not in d: d[key] = value return value else: return d[key]
d = { 'a':1,'b':2,'c':3}print(list(d.keys()))

Important: order of keys and values (and items) are the same 
d = {'a': 1, 'b': 2, 'c': 3} list(d.keys()) à ['a', 'b', d.keys()d.values()d.items()all are iterables 'c'] list(d.items()) à [('a', 1), ('b', 2), ('c', 3)] 

 del d['b']
à dictionaries are now considered ordered (insertion order) àsets are not ordered 


d1 = {'a': 1, 'b': 2} d2 = {'b': 20, 'c': 30}
d1.update(d2) d1 à {'a': 1, 'b': 20, 'c': 30}
d1.update(b=20, c=30)

def func(**kwargs): d = {'a': 1, 'b': 2} print(kwargs)

Deep Copies
can do it ourselves à sometimes requires recursion, have to be careful with circular references this might be needed if we don't want a true deep copy, but only a partial deep copy simpler to use copy.deepcopy from copy import deepcopy à works for custom objects, iterables, dictionaries, etc d1 = d.deepcopy()
