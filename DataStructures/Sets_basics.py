# 1. Create a set with items: "apple", "banana", "cherry"
fruits_set = {"apple", "banana", "cherry", "cherry"}
print(len(fruits_set))
print(fruits_set)

# 2. Add "orange" to it
fruits_set.add("orange")

# 3. Remove "banana"
fruits_set.remove("banana")   # removed successfully
fruits_set.discard("berry")  # no error, even though "berry" wasn't there

# 4. Check if "apple" is in the set
print("apple" in fruits_set)

