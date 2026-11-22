'''
Lists 
'''

# Array (ordered)

# How to find length of array 

# In python you can stor different type of data types 

different_data_type = [1, 2.3, "Jeevan"]

# how we can check type of array 

# using list keyword to init list 
list_keyword = list((1,2,3))

# Different type of collections in python 
# List, Tuple, Set, Dictionary

# Accessing elements in list 

# Iterating over array
for element in different_data_type:
    print("Element is", element)

# Iterating over array using range ie range(lower, upper)
for index in range(len(different_data_type)):
    print("Range element is", different_data_type[index])

# Using in build function enumerate 
for (index, value) in enumerate(different_data_type):
    print(f"The {value} stored in index {index}")

# How we can check if item exists in list 

# Changing the value in list
different_data_type[0] = "2"

# Changing range 
different_data_type[0:2] = "melon"

# insert element 
different_data_type.insert(2, 5)

# append element at end 
different_data_type.append('XYX')

# Extend two list 
different_data_type.extend([1, 1,2,3])

# As in python array is heterogenous so you can append any data type ie. set, tuple dictionary 

'''
Removing elements 
'''

# remove specific element 
different_data_type.remove(1)
print(different_data_type)

# remove specific index 
specific_index_list = [1,2,3,4]

specific_index_list.pop(1)
print(specific_index_list)

# If we don't provide any index 
specific_index_list.pop() # Guess which element will be removed 

# we can use del also to remove particular index element 
del_keyword_list = [1,2,3,4]
del del_keyword_list[1]
print(del_keyword_list)

# we cal delete whole list too
del del_keyword_list # what it will do  


# clear method  - It will remove all elements from list 
clear_list = [1,2,3]
clear_list.clear() 
print(clear_list)

# List comprehension 
# If you want to modify list and store in different variable 
list_comprehension = [1,2,3,4,5]

new_square_list = []
for value in list_comprehension:
    new_square_list.append(value * value)

print(new_square_list)

square_list = [x * x for x in list_comprehension]
print(square_list)

new_comparing_element = []
for value in list_comprehension:
    if value % 2 == 0:
        new_comparing_element.append(value)

print(new_comparing_element)
comparing_element = [x for x in list_comprehension if x % 2 == 0]
print(comparing_element)


'''
Sort list 
'''
unsorted_list = [1,2,3,4,5,6]
unsorted_list.sort()
print(unsorted_list)
unsorted_list.sort(reverse = True)
print(unsorted_list)


# Sort with string will always take capital in priority 

'''
Reverse list
'''
some_list = [1,2,3,4]
some_list.reverse()
print(some_list)

'''
Copy list 
'''
reference_list = [12,3,4,5,6]
reference_list_1 = reference_list
reference_list_1.extend([1,2,3])

print(reference_list, reference_list_1) # What will the response for this 

# so how we can make copy 
list_example = [1,2,3]
copy_list = list_example.copy()
copy_list.append(4)

print(list_example, copy_list)






