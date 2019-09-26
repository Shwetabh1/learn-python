'''
this of java is self in python
__init__ is the constructor
'''


class Robot:
    def __init__(self, name, color, weight): #constructor
        self.name = name
        self.color = color
        self.weight = weight
    def introduce_self(self):
        print('my name is ', self.name)


r1 = Robot('r1', 'metalic', 50)

print(r1.introduce_self())

r2 = Robot('r2', 'ironic', 90)

r2.newProperty = 'yo'

