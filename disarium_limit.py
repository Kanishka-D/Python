for num in range(1,100):
    temp=num
    
    sum=0
    length=len(str(num))
    
    while(temp>0):
      digit=temp%10
      sum=sum+(digit**length)
      temp//=10
      length-=1
      
    if(num==sum):
       print(num)
