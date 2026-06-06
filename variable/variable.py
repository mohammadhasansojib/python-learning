
#* casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


print(type(x))
print(type(y))
print(type(z))

#* Case-Sensitive
# Variable names are case-sensitive.

a = 5
A = 30
# 'a' and 'A' are different

#* variable Naming

# legal names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# illegal names
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""


#* Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

f1, f2, f3 = "Mango", "Banana", "Orange"
print(f1, f2, f3)

#* Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["Cherry", "Apple", "Jack Fruit"]
fruit1, fruit2, fruit3 = fruits
print(fruits)
print(fruit1, fruit2, fruit3)


