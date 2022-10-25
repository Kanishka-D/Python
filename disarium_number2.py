num=int(input())

sum=0
temp=num

length=len(str(num))

while(temp>0):
    digit=temp%10
    sum=sum+((digit**length))
    temp=temp//10
    length-=1


if(num==sum):
    print(f'{num} is a disarium number')
else:
    print(f'{num} is not a disarium number')
    
    
