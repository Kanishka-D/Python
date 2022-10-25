

for i in (56):
    
    num=i
    l=len(str(i))
    result=0
    while(i!=0):
        r=i%10
        result=result+r**l
        i=i//10

    if(num==result):
       print(num)
    
