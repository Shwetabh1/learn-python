def ret_multipe(a, b) -> tuple:
    return (a, b)   #tuple: a read only list

#keywords

#*args make args as tuple

def multiply(*list):
    print(list)


# after seeing this Python will package it as tuple

multiply(1,2,3,4)

#**args make args as object {}

#Scopes

'''
What are lambda functions in python?

While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword
Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned.
'''

double = lambda x: x * 2

print(double(5))

# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
