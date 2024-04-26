#parallel ass
i=0
x = [1,2,3]

i,x[2] = 1,4
print("i is",i)
print("x[] is",x)

#return value 2 ku
def getTwo():
    return (20,30) #() => tuple
x,y = getTwo()
print("x is",x)
print("y is",y)

#ordering compression
lst1 = [3,2]
lst2 = [1,2,3]
print("lst1 < lst2",lst1 < lst2)

#tenary operator
#x = float(input("Enter x :"))
#y = float(input("Enter y :"))

max = x if x > y else y
print("max is ",max)

#special opr
w = 2
z = 1
print("id of w",id(w),"id of z",id(z))
print("w is z",w is z)

b = []
c = []
print("b is c", b is c)

b = ()
c = ()
print("b is c", b is c)

#membership opre
str = "wpa"
print("w in str",'w'in str)

