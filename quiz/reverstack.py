# a=int(input())
# for i in range(a):print("-"*(a-i))


a = int(input("รับค่า = "))       
for i in range(a, 0, -1):
    print()
    for r in range(i):
        print("*", end="")