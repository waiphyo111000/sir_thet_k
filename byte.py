import sys
x = [1,2,3,4]
byt = bytes(x)
print("types of byt",byt[0])
#byte so unmutable

y = [4,5,6,6]
by = bytearray(y)
by[3]=7
print("by array is",by)

print("size of x",sys.getsizeof(x))