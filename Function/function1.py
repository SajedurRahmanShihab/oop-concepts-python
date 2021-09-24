def my_function():
    print("Hello from a function")


my_function()
print(my_function)

# function with param


def my_function1(firstName):
    print("Mr. " + firstName)


my_function1("Shihab")


def my_function2(firstName, lastName):
    print(firstName + " " + lastName)


my_function2("Sajedur Rahman", "Shihab")


# * Arbitrary Arguments, *args
def my_function4(*name):
    print("Random name is: " + name[3])


my_function4("Sajedur", "Rahman", "Shihab", "Rifat", "Saiful")


# Keyword Arguments
# If the number of arguments is unknown, add a * before the parameter name
# This way the function will receive a tuple of arguments, and can access the items accordingly
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="John", child2="Doe", child3="david")


# Arbitrary keyword Arguments, **kwargs
# This way the function will receive a dictionary of arguments, and can access the items accordingly
# If the number of keyword arguments is unknown, add a double ** before the parameter name
def my_function(**kid):
    print("His last name is " + kid["anotherLastName"])


my_function(fname="Tobias", lname="Refsnes", anotherLastName="Rahman")


# Default Parameter Value
def my_function(country="Bangladesh"):
    print("I am from " + country)


my_function("Bangladesh")
my_function()

# Passing a List as an Argument


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# Return Values
def my_function(x):
    return 5 * x


print(my_function(3))

# The pass Statement
#  function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.


def myfunction():
    pass


# Recursion
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
