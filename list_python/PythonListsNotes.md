**Lists in Python.**

A list is a data type that allows you to store various types data in it. 
List is a compound data type which means you can have 2 different data types under a list, for example we can have integer, 
float and string items in the same list.In short, list is ordered collection of objects.

**Coding:**
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

**Output of above program:**
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


List methods - insert(),append(),extend() 
------------------------------------------------------------------------------------------------------------------------------------

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

**Output of above program:**
```
Displaying elements of the list [1, 2, 3, 100, 4]
After adding element to the end of the list [1, 2, 3, 100, 4, 99] 
Numbers is stored at 139909621338880 location 
Numbers is stored at 139909621824192 location 
After adding elements to the end of the list [1, 2, 3, 100, 4, 99, 11, 22, 111, 222] 
```
**Update list**

```
# list of numbers
numbers = [1, 2, 3, 4]
print("Displaying the elements of the list {} ".format(numbers))
# Changing the value of 3rd item
numbers[2] = 100

# list: [1, 2, 100, 4]
print("Displaying the elements after modifying the index 2(3rd pos) of the list {} ".format(numbers))

print("Before updating {} - number address location ".format(id(numbers)))
# Updating the values of 2nd to fourth items
numbers[1:4] = [11, 22, 33]
print("After updating {} - number address location ".format(id(numbers)))
# list: [1, 11, 22, 33]
print(numbers)
```
**Output of above program:**

```
Displaying the elements of the list [1, 2, 3, 4] 
Displaying the elements after modifying the index 2(3rd pos) of the list [1, 2, 100, 4] 
Before updating 140333568000768 - number address location 
After updating 140333568000768 - number address location 
[1, 11, 22, 33]
```
**Delete operation in list**

```
# list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Deleting 2nd element
del numbers[1]

# list: [1, 3, 4, 5, 6]
print(numbers)

# Deleting elements from 3rd to 4th
del numbers[2:4]

# list: [1, 3, 6]
print(numbers)

# Deleting the whole list
del numbers

# list of numbers
numbers = [1, 2, 3, 4, 5, 6]

print("Printing the list")
print(numbers)

print(numbers.pop())
if 3333 in numbers:
    numbers.remove(3333)
print(numbers)

numbers.clear()
print(numbers)
```
**Output of above program**
```
Output
Printing the list
[1, 2, 3, 4, 5, 6]
6
[1, 2, 3, 4, 5]
[]
```

**Other operations supported on list**
```
numbers = [2,12,41,15,-6,2,33,2]
print("Displaying the list {}".format(numbers))
print("The number of occurances of number 3 is {}".format(numbers.count(3)))
print("The number of occurances of number 2 is {}".format(numbers.count(2)))
print("The index of element 12 in the list {}".format(numbers.index(12)))
print("Displaying element in sorted order {}".format(sorted(numbers)))
print("The len of list is {}".format(len(numbers)))
print("The max element of the list {}".format(max(numbers)))
print("The min element of the list {}".format(min(numbers)))
print("The sum of elements in the list {}".format(sum(numbers)))
numbers.sort()
print("Sorted the list using sort method mutates the list {}".format(numbers))
str = "abc"
elem = list(str)
print("Conversion of string  - {} to list -{} ".format(str,elem))
```
**Output of above program**
```
Displaying the list [2, 12, 41, 15, -6, 2, 33, 2]
The number of occurances of number 3 is 0
The number of occurances of number 2 is 3
The index of element 12 in the list 1
Displaying element in sorted order [-6, 2, 2, 2, 12, 15, 33, 41]
The len of list is 8
The max element of the list 41
The min element of the list -6
The sum of elements in the list 101
Sorted the list using sort method mutates the list [-6, 2, 2, 2, 12, 15, 33, 41]
Conversion of string  - abc to list -['a', 'b', 'c'] 
```
