# import math
a =  [int(x) for x in input().split()]
# price = math.ceil(((a[0]*60)+a[1])/60)
# print((price-1)*30)

def const(h,m):
    if h>0:
        h+=-1
        if m>0:
            h+=1
        return h*30

    elif h==0:
        return "0"
print(const(a[0],a[1]))