#nested Condition

myan = float(input("Enter Myanmar Marks : "))
eng = float(input("Enter English Marks : "))
math = float(input("Enter Math Marks : "))

pass_mark = 50
if myan >= pass_mark and eng >= pass_mark and math >=pass_mark:
    print("Pass all")
else:
    if myan <= 39:
        print("Myanmar fail")
        if eng <= 39:
            print("English fail")
        if math <= 39:
            print("Math fail")
print("End")