# tuples are declared using () and elements are separated using comma
# tuples are immutable

# declare empty tuple
empty = ()
print(type(empty))

# declare tuple using constructor
c = tuple('Prasad')
print (c)

# declare tuple using values
t = ("Prasad", "Honrao", 37, "Pune")
print (t)

# access tuple element using indexer
print('First element in tuple is' , t[0])

# find tuple length using len
print('Tuple length is ', len(t))

# iterate through tuple
for item in t:
    print(item, end=' ')
print('')

