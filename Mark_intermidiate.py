no_of_sub = int(input("Enter number of subject : "))
marks = []
pass_mark = 50

for i in range(no_of_sub):
    w = ["Myanmar","English","Math","501","502","503"]
    mark = float(input("Enter Marks for sub "+w[i]+" : "))
    marks.append(mark)
print("Marks ",marks)

Pass = True
for mark in marks:
    Pass = Pass and mark >= pass_mark

if Pass:
    print("pass")
else:
    print("Fail")



