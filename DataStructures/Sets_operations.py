'''
operations include - union, intersection, difference, ser_difference 
'''

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

# union of set 1 and set 2
print(set1.union(set2))
print(set1 | set2)

# intersection of both sets.
print(set1.intersection(set2))
print(set1 & set2)

# difference - gives you items that are in the first set, but not in the second.
print(set1.difference(set2))
print(set1 - set2)

# symmetric difference - excludes the common elements
print(set1.symmetric_difference(set2))
print(set1 ^ set2)
