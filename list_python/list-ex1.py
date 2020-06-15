browser = ["firefox","chrome","safari"]
print("The items in list {}".format(browser))

# append adds the element to the end of the list
browser.append("edge")
print("After adding {} element to end of the list : {}".format("egde",browser))

# adds/inserts element to specific position
browser.insert(1,"mozilla")
print("After adding {} element to first index of the list : {}".format("mozilla",browser))

# adding element using slicing
browser[2:3] = ['Apple safari','Microsoft IE']
print("The elements in the list after updating using slicing {}".format(browser))

# update the list using indexing
browser[1] = "google chrome"
print("Update the list element in first position {}".format(browser))

# remove the element if present else ValueError exception
if "ie" in browser:
    browser.remove("ie")


# List slicing
print("The last element of the list {}".format(browser[-1]))
print("The first two element of the list {}".format(browser[:2]))
print("The last two element of the list {}".format(browser[-2:]))

numbers = list(range(0,16))
print("There are {} elements in list :{}".format(len(numbers),numbers))

# iterate over list and condition in list
print("Even numbers between 0 to 15")
for number in numbers:
   if number%2 == 0:
      print(number,end=' ')

# count occurance of item - if item present the it returns the occurance else if not present the returns 0
beverages = ['coke','pepsi','slice','thumbs up','thumbs up']
print("The beverages list has thumbs up  repeated {} times".format(beverages.count('thumbs up')))
if 'miranda' in beverages:
   print("The beverages list has miranda  {} times".format(beverages.count('miranda')))

