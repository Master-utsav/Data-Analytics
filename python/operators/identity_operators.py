
# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)  # True because both refer to the same object
print("a is c:", a is c)  # False because they are different objects
print("a is not b:", a is not b)  # False because they are the same object
print("a is not c:", a is not c)  # True because they are different objects
