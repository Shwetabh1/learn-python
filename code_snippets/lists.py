"""
I have used lists readily while converting my js solutions to python.
You can find code samples for all these in competitive_coding_in_py
"""

# add some theory, library methods for reference
# some list
some = ['a', 'b', 'i', 'c', 'i', 'd']

# count occurence of element
count = some.count('i')

# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

# count element ('a', 'b')
count = random.count(('a', 'b'))

#difference between list and range object
#list occupies a lot of memory.

#We can use lists as deque 

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
'Eric'
queue.popleft()                 # The second to arrive now leaves
'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

# you can create lists using lambdas

# A list Comprehension

'''
A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. 
The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
'''

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

squares = [x**2 for x in range(10)]


#Use a collections.deque for both
#rotate lists
a = [1,2,3,4,5]
a.append(a.pop(0))

'''Let's try to draw similarity between JS list functions and Python
1. list.append(x)    arr.push(x)
2. list.insert(i, x) arr.splice(1, 0, item)
3. list.remove(x) # removes the first element that is x
4. list.clear() or del a[:] In JS array.length = 0 || arr = [
5. sort is same.    
] 
'''


#nested lists

matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]


[[row[i] for row in matrix] for i in range(4)]

arr = [1,2,3,4,5,6,7,8]

#del operator kindof slice in js
del a[0]
del a[2:4]
del a[0:]
del a


#Sequence Type in Python [TODO]



