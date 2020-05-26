lst=[10, 20, -73, "David", 69]
print(lst)
print(lst[3])
print(lst[1:3])
print(lst*4)
print(len(lst))

lst.append(45)
lst.remove("David")
print(lst)
del(lst[0:2])   #remove items from list starting from location 0 up till 2
print(lst)
lst.remove(lst[0])
print(lst)

#lst.clear()
#print(lst)

print(max(lst))
print(min(lst))

lst.insert(2, 99) #will insert value into a particular list location 
print(lst)

lst.sort(key=None, reverse=True)
print(lst)

"""
country = ["Nigeria", "Germany", "Egypt"]
country.append( "Greece")
print(country)
country.remove(country[1])
print(country)
country.insert(2, "Italy")
print(country)"""