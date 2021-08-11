a=int(input())
g=[]
q=0
y=[]
while True:
    b=int(input())
    if b==0:
        break
    else:
        g.append(b)
        if b==a:
            q+=1
            y.append(q)
        else:
            q=0
y.sort()
print(y[-1])
print(g.count(a))