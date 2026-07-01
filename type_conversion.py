#Explicit Conversion

a="9"
b="9"
c= int(a)+int(b)
print(c)
print(bool(a))
print(complex(a))

#Implicit Conversion

# Defining an integer and a float
num_int = 10       # <class 'int'>
num_float = 5.5    # <class 'float'>

# Adding the two different data types
result = num_int + num_float

# Displaying the outcome and its automated type
print("Value:", result)
print("Data Type:", type(result))
