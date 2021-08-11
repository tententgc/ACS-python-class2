a, b = input().split(" ")
z = []
for i in range(len(a)):
    if a[i] == "1" and b[i] == "1":
        z.append('1')
    elif a[i] == '1' or b[i] == "1":
        z.sppend('1')
    else:
        z.append("0")
print("".join(z))
