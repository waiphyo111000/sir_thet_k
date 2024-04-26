no_of_sub = int(input("Enter number of subject : "))
marks = []
pass_mark = 50
Pass = True

for i in range(no_of_sub):
    w = ["Myanmar","English","Math","501","502","503"]
    mark = float(input("Enter Marks for sub "+w[i]+" : "))
    Pass = Pass and mark >= pass_mark
    
if Pass:
    print("Success")
else:
    print("Failed")

    