#BYTE AND BYTEARRAY
#insertion and deletion don't work with bytes and bytearray

lst1 = [20, 30, 40, 255]
b = bytes(lst1)
print(type(b))

b1 = bytearray(lst1)
print(type(b1))