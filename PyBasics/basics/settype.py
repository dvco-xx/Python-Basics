#SET TYPE

#To declare a set
s = {10, 20, 30, 40, "xyz"}

s1 = {} #empty set
print(s)
print(s1)
 
#To add object into a set
s.update([88, 99])
print(s)
 
#To delete/remove object from a set
s.remove(88)
print(s)
 
f = frozenset(s)
# # A frozen set accepts a set & freezes it so that it can no longer be manipulated.
