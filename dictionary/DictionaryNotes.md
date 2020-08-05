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

**1. Using fromkeys**
fromkeys takes iterable as first argument and second argument is default value to the keys.``
```


d = dict.fromkeys(['a', (0,0), 100], 'N/A')

for (key,val) in d.items():
    print("{} - {}".format(key,val))

output:
a - N/A
(0, 0) - N/A
100 - N/A

```

**2. Dictionary Comprehension:**
```
   squares_numbers = {
      str(i): i*i for i in range(1,10)
   }
   print(squares_numbers)
   
   Output:{'1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}
```


**Assigning(adding) value from dictionary**

Below syntax creates(adds) key if key is NOT PRESENT in the dictionary

d[key] = value  

Example:

d = { '1':'a','2':'b','3':'c'}

d['4']='e'

Above statement will add key '4' in to dictionary d.

**Fetching value from dictionary**

Below syntax retrieves the key in the dictionary if its PRESENT in the dictionary.

d[key] as an expression, it returns the value for specified key in the dictionary, if key is not present then it throws KeyError exception 


d.get(key) - returns value if key is found,otherwise the method returns 'None'.

d.get(key, 'N/A') - returns value if key is found,otherwise 'N/A'.

**Membership testing**

key in d - True if key is in d, False if it is not

len(d) - The len() on dictionary returns number of items PRESENT in dictionary

**Remove items of dictionary***

1. Removes all items
d.clear() - makes dictionary empty - {}

2. Delete specific item


del d[key] - removes item for the matching key if present else raised KeyError exception

d.pop(key) - removes element with that key from dictionary 'd' and alse returns the corresponding value 

d.pop(key, default) - returns default is key was not found à exception KeyError if key is not in d

```
def insert_if_not_present(d, key, value):
   if key not in d: 
      d[key] = value 
      return value 
   else: 
      return d[key]
```
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
