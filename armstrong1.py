num=int(input())


sum=0
result=0
temp=num
while(temp>0):
    result+=1
    temp//=10

temp=num
while (temp>0):
    single_digit=temp%10
    sum=sum+(single_digit**result)
    temp//=10

if(num==sum):
    print(f"{num} is a armstrong number")
else:
     print(f"{num} is not a armstrong number")
