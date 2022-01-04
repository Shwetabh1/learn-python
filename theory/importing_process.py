print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")
# What is __name__ == __main__ check?
'''
1. When the Python interpeter reads a source file, it first defines a few special variables. In this case, we care about the __name__ variable.
2. If you are running your module as the main program, e.g. python3 foo.py, it is as if __name__ == __main__ is assigned at the top.
3. If our module is imported then __name__ will be assigned the value as foo to our module's name variable
'''
