num=int(input())
length=len(str(num))


result=0
temp=num
while temp>0:
    single_digit=temp%10
    result=result+(single_digit**length)
    temp//=10
    length=length-1

if(num==result):
     print(f"{num} is a disarium number")
else:
     print(f"{num} is not a disarium number")
    
