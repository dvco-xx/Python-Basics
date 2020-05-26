#A dictionary type uses keys and values.
#Keys and values can be of any object type e.g. 1:"david", 3":"david"

dict1 = {1:"david", 2:"R", 3:"Weasel", "boy":"girl", "joy":5}
print(dict1)

#indexing
print(dict1[2])

print(dict1.keys())  #display only keys

k = dict1.keys()     #loop through each key position in dict1 and print
for i in k:
    print(i)

print(dict1.values()) #display only values

v = dict1.values()    #loop through each 'value' position in dict1 and display them
for i in v:
    print(i)
    
print(dict1.items())  #displays all dict1 items in pairs of [('k','v'), ('k','v')...]


#deleting from dictionary

del(dict1[2])
print(dict1)  #check to see if key 2 is removed

x = dict1.copy()
print(x)

