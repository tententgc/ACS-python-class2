# I=1 V=5 X=10 L=50 C=100 
i =0 
v=0
x=0
l=0
c=0
for num_input in  range(int(input())+1):
    c = num_input//100
    num_input =num_input%100
    g=num_input//10
    if g ==9:
        x+=1
        c+=1
    elif g==8:
        x+=3
        l+=1
    elif g==7:
        x+=2
        l+=1    
    elif g==6:
        x+=1
        l+=1    
    elif g==4:
        x+=1
        l+=1    
    elif g==3:
        x+=3    
    elif g==5:
        l+=1  
    elif g==2:
        x+=2
    elif g==1:  
        x+=1
    num_input=num_input%10
    g=num_input
    if g == 9:
        x+= 1
        i += 1
    elif g == 8:
        i += 3
        v += 1
    elif g == 7:
        i += 2
        v += 1
    elif g == 6:
        i += 1
        v += 1
    elif g == 4:
        v += 1
        i += 1
    elif g == 3:
        i += 3
    elif g == 5:
        v += 1
    elif g == 2:
        i += 2
    elif g == 1:
        i += 1

print(i,v,x,l,c)


