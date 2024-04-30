st = "wpa is for myat thiri maung "

print("string with start",st.startswith("w"),"\n")
print("string is capitalize",st.capitalize())
print("str endwith",st.strip().endswith("maung"))


#num_str = input("Enter number :")
#while not num_str.isdigit():#digit or int yes or no
#    print("not number")
#   num_str = input("Enter number :")
#print("Num is int ",num_str)

a = "wpa"
b = "mee"
print("mee is {wpa} and wpa is {mee}".format(wpa=a,mee=b))#most used format

print("decimal 3 is {:d}".format(4*4))
print("float is {:.2f}".format(3.5*2.1))
        
