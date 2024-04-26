lst = [1,2,3,4]

for i in range(len(lst)):
    print("lst",lst[i]*2)
    
print(lst)

#key only
dir = {"user1":"wpa","user2":"meemee"}

for i in dir:
    print("dir is ",i)
    
#key and value
for i,j in dir.items():
    print("Key is ",i,"Value is ",j)