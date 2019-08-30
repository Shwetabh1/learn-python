"""
 * Given a String reverse the words in it.
 * EXAMPLE: "How deep    is     your Love?"
 * OUTPUT : "woH peed si ruoy evoL"
 * trim the whitespaces if it exists
 * Python strings are immutable, meaning the memory allocated to each cannot be written to, making true "in place" reversals impossible .
"""
# My JS Solution converted to Python

import re


def reverse(str):
    rev = re.split("", str)
    rev.reverse()
    return "".join(rev)

def reverseWords(str):  
	auxStr = re.split("\s+", str)
	for index, word in enumerate(auxStr):
		auxStr[index] = reverse(word)

	return " ".join(auxStr)

string1 = "How deep is your Love?"
string2 = "DC is better than             Marvel.      "

print(reverseWords(string1))
print(reverseWords(string2))