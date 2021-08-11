z=[]
q=[]
a=0
b=0
c=0
g=[]
d=0
while True:
    a=int(input())
    if a==0:
        break
    else:
        g.append(a)
for i in g:
    if d==i:
       c+=1
       if c>=b:
           b=c
           q.append(i)
           z.append(c)
    else:
        d=i
        c=0
print(q[-1])
print(z[-1]+1)
