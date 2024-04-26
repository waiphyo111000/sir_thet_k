#ques: sum of tenth number in 1 to 100

counter = 0
total = 0

while(counter <= 100):
    if counter%10 == 0:
        print("Counter is ",counter)
        total += counter
    counter +=1
print("total",total)