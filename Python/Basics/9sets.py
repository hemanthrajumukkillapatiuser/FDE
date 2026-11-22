'''
Set
'''

# Set is unorderd, doesn't contain duplicate, and are static 
set_example = {1,2,3,4}
set_example_1 = set((1,2,3,4))

# We can store heterogenous values in set too
set_example_2 = {1, 2, 3, 0, False, True,"XYZ"}

# We cannot change existing values in set but we can add new element 
set_example.add(5)
print(set_example)


# extending two sets
set_example.update(set_example_1)
print(set_example)

'''
Remove item 
'''
remove_set = {1,2,3,4}
remove_set.remove(1)
#remove_set.remove(5) # if element doesn't exist it will raise exception

remove_set.discard(5) # it will not raise any exception
print(remove_set)
remove_set.pop() # what will be the response of this one
remove_set.clear()
del remove_set

'''
Looping over set 
'''

'''
Joining set 
'''

# Union or update (joins elements of two sets)
first_set = {1,2,3,4}
second_set = {4,5,6,7}

print(first_set.union(second_set))
first_set.update(second_set)
print(first_set)
print(first_set | second_set)

# intersection - Keeps only duplicates
print(first_set.intersection(second_set))
print(first_set & second_set)
# first_set.intersection_update(second_set)
# print(first_set)

# Difference - values that are only present in first set
print(first_set.difference(second_set))
print(first_set - second_set)
# first_set.difference_update(second_set)
# print(first_set)

# Symmetric difference -> Elements that are not present in both set 
symetric_1 = {1,2,3,4}
symetric_2 = {1,6,7}
print(symetric_1.symmetric_difference(symetric_2))
print(symetric_1 ^ symetric_2)
# symetric_1.symmetric_differencee_update(symetric_2)
# print(symetric_1)


'''
Frozen set
'''
# it cannot be changed 
example_frozen_set = frozenset({1,3,4,5})
print(type(example_frozen_set))