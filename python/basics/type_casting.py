a = 123
b = 1.23

print (type (a))
print (type (b))

c = a + b # implicit type casting
print (c)
print (type (c))

a = float(a) # explicit type casting
print ("after conversion" , type(a))