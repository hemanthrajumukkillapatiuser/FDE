'''
Tuples
'''

# Tuples are same as array but these are static and cannot be changed directly

tuple_example_without_brackets = 1,2,3,4 
tuple_example_with_brackets = (1,2,3,4)


# Create empty tuple
empty_tuple = ()

# Create one element tuple  
one_element_tuple_0 = (1) # What type will this be 
print("one element tuple", type(one_element_tuple_0))
one_element_tuple_1 = (1, )
print("XYX", type(one_element_tuple_1))

# init via tuple constructor 
constructor_tuple = tuple((1,2,3))

'''
Accessing tuples 
Same as array 
'''

'''
Updating tuples 
'''
# As tuples are static and cannot be changes we can modify it via converting into list then convert into tuple

example_tuple_modify = (1,2,3)
example_tuple_list = list(example_tuple_modify)
example_tuple_list.append(7)
converted_tuple = tuple(example_tuple_list)
print(converted_tuple)


'''
Unpacking tuples
'''
# packing tuples
packing_tuple = (1,2,3)

first, second, third = packing_tuple

print(type(first), second, third)

# left side variable should be equal to tuple len 
# if we want to store uneven number use list by marking * 

first, *remaining = packing_tuple
print(first, remaining, type(remaining))

more_tuple = (1,2,3,3,4,5,6)
first, *middle, last = more_tuple

'''
Loop over tuples
'''
# same as list 

'''
Join tuples
'''
# same as array 

'''
Tuple methods 


count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''