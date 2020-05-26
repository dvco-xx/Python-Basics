s = "You are awesome "
print(s)

s1 ="""You are the 
creator of your 
destiny"""

print(s1)
print(s[4])     #display string element at location 3
print(s*5)      #repeat string 5 times
print(len(s1))  #length of string s1
print(len(s))   #length of string s1

#slicing operations
print(s[:8])         #print all characters from position 0 till 8 (excluding 8)     
print(s[8:])         #print all characters from position 8 till the end of string
print(s[-3:-1])      #display characters starting from end of string up till position -4 (excluding character at -1)
print(s[0:9:2])      #Jump two characters from start of string till 9th character (included) i.e Y_u_a_e_a
print(s[15::-1])     #reverse string s
print(slice(s[0], s[6], s[11]))
print(s)

#print(s.lstrip())
#print(s.rstrip())
#print(s.strip())

print(s.find("awe", 0, len(s)))
print(len(s))
print(s.count("a"))
print(s.replace("awesome", "super"))
print(s.lower())
print(s.upper())
print(s.title())

x=10
y=20.54
z=True
w="I am the best"
print(x, y, z, w)