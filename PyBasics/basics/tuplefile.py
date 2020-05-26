tpl=(40, 50, 40, "xyz")
tpl1=(76,) #while declaring a tuple with a single value *-+*-*+, end with a comma or else it is interpreted to be an integer value
print(tpl)
print(tpl1)

#functions that can be performed on a tuple include indexing, repetition, counting, max/min, len, location indexing
print(tpl[3])           #locate the element at index 3
print(tpl*3)            #repeat the elements in tuple 3 times
print(tpl.count(40))    #count how many times 40 appears in tuple
print(tpl.index("xyz")) #locate the index of 'xyz'

lst=[25, 50, 75, 100]
print(type(lst))
tpl2 = tuple(lst) #converts sequence e.g list type to tuple using tuple in-built function
print(type(tpl2))
print(tpl2)