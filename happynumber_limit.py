
def happynum(num):
   
   sum=0
   while(num>0):
     digit=num%10
     sum=sum+(digit**2)
     num//=10
   return sum
    


for number in range(1,101):
  temp=number

  while(temp!=1 and temp!=4):
    temp=happynum(temp)


  if(temp==1):
    print(number)
