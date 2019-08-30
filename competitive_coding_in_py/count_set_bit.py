"""
Count the number of set bits in an Integer.
"""

# Approach 1: Use Library function

# def countSetLibrary(num):
#     binary_representation = bin(num)
#     count = 0
#     # count the number of ones
#     return binary_representation.count(1) 

# print(countSetLibrary(8))
# print(countSetLibrary(0))

# Approach 2: Simple Loop

def countSetSimple(num):
    count = 0
    while num:
        count += num & 1
        num = num >> 1  
         
    return count

print(countSetSimple(8))
print(countSetSimple(0))
