# determine if a string has all unique characters.

""" There are various ways to go about it.
Use of hashmap, sets or simple loop. I will try to implement it in each way"""

# I am using a set and doing length comparison

def has_unique_char_set(str):
    if not str.strip():
        return False
    return len(set(str)) == len(str)

# I am using a map/dictionary and doing a length comparison

print("Set", has_unique_char_set(""))
print("Set", has_unique_char_set("Z"))

# I am using a map
def has_unique_char_dictionary(str):
    obj = {}
    if not str.strip():
        return False
    for char in str:
        if char in obj:
            obj[char] = obj[char]+1
        else:
            obj[char] = 0       
    for val in  obj.values():
        if val >= 1:
            return  False
    return True       

print("Map", has_unique_char_dictionary("HELLOOO"))
print("Map", has_unique_char_dictionary("HEY"))
print("Map", has_unique_char_dictionary(""))

#simple for loop
def has_unique_chars_loop(str):
    if str is None:
        return False
    for char in str:
        if str.count(char) > 1: #returns the number of occurrences of a substring in the given string.
            return False
    return True

print("loop", has_unique_chars_loop("HeLoO"))
