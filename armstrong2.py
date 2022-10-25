num=int(input())
length=len(str(num))

sum=0
temp=num

while(temp>0):
    digit=temp%10
    sum=sum+(digit**length)
    temp=temp//10


if(num==sum):
    print(f'{num} is a armstrong number')
else:
    print(f'{num} is not a armstrong number')
