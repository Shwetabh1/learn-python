"""
I will not be writing down codes for all these as I have used below readily while converting my js solutions to python.
You can find code samples for all these in competitive_coding_in_py
1. if elif else 

2. for
There are diff styles.
> in
> range
> loops can have else
> continue break

3. Pass: the pass statement does nothing particular, but it can act as a placeholder.

4. while

5. functions
any number of argument = *args

6. Lambda 
They are nothing but syntactic sugar for a normal function definition



"""

def attach_greeting(n):
     return lambda x: x + n

f = attach_greeting('Hey: ')
print(f('shwetabh'))
