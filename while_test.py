lst = [1,2,3,4,5]

user_no = int(input("Enter user number : "))
found = False
index = 0

while not found and index < len(lst): #input ko ma find thy yin 
    if user_no == lst[index]:
        print("Index is ", index)
        found = True
    else:
        index += 1
        