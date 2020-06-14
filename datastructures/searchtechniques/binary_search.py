def binary_search(input:'List',key:'int')->'int':
    print("The input is : {} and key to search is : {}".format(input,key))
    left = 0
    right = len(input) - 1
    result = -1
    while(left <= right):
        mid = (left + right) //2
        if input[mid] == key:
            result = mid
            break
        elif key > input[mid]: 
            left = mid + 1
        else:
            right = mid - 1

    return result

input = [100,2,5,24,10,11,1]
# Pre-requisite of binary search - Elements needs to be in sorted order
input.sort()
key = 1
print(binary_search(input,key))
key = 100
print(binary_search(input,key))
key =30
print(binary_search(input,key))
