

def happynum(num):
   
   sum=0
   while(num>0):
     digit=num%10
     sum=sum+(digit**2)
     num//=10
   return sum
    

number=int(input())
temp=number

while(temp!=1 and temp!=4):
    temp=happynum(temp)


if(temp==1):
    print(f"{number} is a happpy number")
else:
    print(f"{number} is a not happpy number")
