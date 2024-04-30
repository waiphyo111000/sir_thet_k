lst1 = [10,21,33,40,50,60]
for i in lst1:
    if i % 2 == 0:
        print("This is even No :",i)
        

for index,value in enumerate(lst1):
    lst1[index] *= 2
print("List is ",lst1)

l=[100,200]
lst1.extend(l)
print("Extend is ",lst1)

print("pop is ",lst1.pop(),"list is ",lst1)