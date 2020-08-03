Lists in Python. 
A list is a data type that allows you to store various types data in it. 
List is a compound data type which means you can have 2 different data types under a list, for example we can have integer, 
float and string items in the same list.In short, list is ordered collection of objects.

** Coding:**
```
numbers = [11, 22, 33, 100, 200, 300]
print("First element is {}".format(numbers[0]))
try:
    print(numbers[6])
except IndexError as e:
    print("There is no element at the index")

print("The element at the last position is {}".format(numbers[-1]))
print("List items from 2nd to 3rd positions are {} ".format(numbers[1:3]))
print("First three elements of list {}".format(numbers[:3]))
print("Elements from 4th position till end of the list {}".format(numbers[3:]))
print("Whole list {}".format(numbers[:]))
```

------------------------------------------------------------------------------------------------------
** Output of this program: **
------------------------------------------------------------------------------------------------------
```
First element is 11
There is no element at the index
The element at the last position is 300
List items from 2nd to 3rd positions are [22, 33] 
First three elements of list [11, 22, 33]
Elements from 4th position till end of the list [100, 200, 300]
Whole list [11, 22, 33, 100, 200, 300]
```
------------------------------------------------------------------------------------------------------------------------------------

** list methods - insert(),append(),extend() **

```
numbers = [1, 2, 3, 4]

# adding item at the desired location using insert method
# adding element 100 at the fourth location
numbers.insert(3, 100)

# list: [1, 2, 3, 100, 4]
print("Displaying elements of the list {}".format(numbers))
numbers.append(99)
print("After adding element to the end of the list {} ".format(numbers))

# Below statement is same as  : numbers = numbers + [11, 22] - Mutates lists  creating new list
print("Numbers is stored at {} location ".format(id(numbers)))
numbers.extend([11, 22])
print("Numbers is stored at {} location ".format(id(numbers)))
print("After adding elements to the end of the list {} ".format(numbers))
```

------------------------------------------------------------------------------------------------------
Output of this program:
------------------------------------------------------------------------------------------------------
```
Displaying elements of the list [1, 2, 3, 100, 4]
After adding element to the end of the list [1, 2, 3, 100, 4, 99] 
Numbers is stored at 139909621338880 location 
Numbers is stored at 139909621824192 location 
After adding elements to the end of the list [1, 2, 3, 100, 4, 99, 11, 22, 111, 222] 
```
