st = "wpa is for myat thiri maung "

print("string with start",st.startswith("w"),"\n")
print("string is capitalize",st.capitalize())
print("str endwith",st.strip().endswith("maung"))

num_str = input("Enter number :")
while not num_str.isdigit():#digit or int yes or no
    print("not number")
    num_str = input("Enter number :")
print("Num is int ",num_str)
        
