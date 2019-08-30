import re
#split works differently here. Instead of string use regex
str = "hey"
re.split("", str)

course = "HEY"

len(course) # get the length

course[0]

course[-1] # reverse way 

course[0:3] #doesn't include char at index 3

#strings are immutable

#escape sequences

message = "hey \" "

first = "Shwetabh"

last = "Shekhar"

full = f"{len(first) + last}"

#the usual string functions
course.upper()
course.lower()
course.title()
course.strip() #lstrip #rstrip
course.find("pro")
course.replace("P", "-")

#Mutabel Immutable in Python

a = "Foo"
# a now points to "Foo"
b = a
# b points to the same "Foo" that a points to
a = a + a
# a points to the new string "FooFoo", but b still points to the old "Foo"

print a
print b
# Outputs:

# FooFoo
# Foo

# Observe that b hasn't changed, even though a has.

# typecast using this str(i)