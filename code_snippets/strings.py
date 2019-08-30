course = "HEY"

len(course)

course[0]

course[-1] # reverse

course[0:3] #doesn't include char at index 3

#strings are immutable

#escape sequences

message = "hey \" "

first = "Shwetabh"

last = "Shekhar"

full = f"{len(first) + last}"

course.upper()
course.lower()
course.title()
course.strip() #lstrip #rstrip
course.find("pro")
course.replace("P", "-")

in operator
not operator

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