str = input("Enter words : ")
word = str.split()
res = ""
for w in word:
    res = res + " " + w[::-1]
print("word is",res)