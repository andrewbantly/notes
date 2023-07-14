"""
A set is an unordered collection with no duplicate elements. Sets are iterable and mutable. Order of elements in a set is undefined and is unchangeable. Type of elements in a set need not be the same, various mixed-up data type values can also be passed to the set.

The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

The disadvantages of sets are that they are unordered, have limited funtionality compared to lists (they do not support methods like append or pop), sets can consume more memory than lists (especially for small datasets) because each element in a set requires additional memory to store a hash value, and sets are less commonly used so there may be fewer resources or libraries available for working with them. 

Note: to create an empty set you have to use set()
"""
andrew = set("andrew")
print(andrew)
# output: {'d', 'r', 'n', 'a', 'w', 'e'}

mixed = set([98, "Earth", True, "Hello", 39])
print(mixed)
# output: {True, 98, 39, 'Hello', 'Earth'}


### METHODS

# ADD
"""
Adds an element to a set
"""
andrew = set("andrew")
andrew.add('h')
print(andrew)
# output: {'e', 'r', 'd', 'h', 'a', 'w', 'n'}

# REMOVE
"""
Removes an element from a set. If the element is not present in the set, raise a KeyError
"""
andrew = set("andrew")
andrew.remove('w')
print(andrew)
# output: {'a', 'd', 'n', 'e', 'r'}