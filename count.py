str = "wpa is wpa"
sub_str = "wpa"
count = 0
index = 0

while index < len(str):
    another_str = str[index:index+len(sub_str)]
    if sub_str in another_str:
        count += 1
    index += 1
print("Count is ",count)