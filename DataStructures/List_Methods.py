#LIST METHODS...

## append()
# Add "pineapple" to the end of the fruits list using .append()
fruits = ["apples", "mangoes", "oranges", "grapes", "avacodoes"]
fruits.append("pineapples")
print(fruits)


## extend(list)
# add sequence to the list
nums = [1,5,6]
nums.extend([2,3,4])
print(nums)

## insert(index, value)
'''Adds an item at a specific position in the list
Moves the rest of the list to the right
task: Insert "blueberries" at index 2 (so it appears before "oranges")'''
fruits.insert(2,"blueberries")
print(fruits)

## remove(value)
'''Searches for the first occurrence of the given value. Removes it from the list.
If the value is not found, it throws an error'''
fruits.remove("avacodoes")
print(fruits)
#fruits.remove("cherry") # ValueError


## pop(index) — Remove by position
'''Removes and returns the item at the given index
If no index is given, it removes the last item
Unlike .remove(), .pop() works by position, not value'''
#Task:
#Use .pop() to remove the last fruit, and store it in a variable
last_item = fruits.pop()
print(last_item) #Print the removed fruit
print(fruits) # Print the updated list


## sort()
'''
Sorts the list alphabetically (for strings) or numerically (for numbers)
Changes the original list (doesn't return a new list)
'''
fruits.sort()
print(fruits)


## reverse()
''' Reverses the list in place. Also modifies the original list '''
fruits.reverse()
print(fruits)



# nested list

matrix = [
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90]
]

# 1. Print the entire second row
print(matrix[1])
# 2. Print the value 80 by using indexing
print(matrix[2][1])

for row in matrix:
    for val in row:
        print(val, end=' ')

