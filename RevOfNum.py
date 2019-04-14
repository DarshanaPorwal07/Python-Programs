reverse=0
num=int(input("enter the number"))
while num>0:
    a=num%10
    reverse=(reverse*10)+a
    num=num//10
print("reverse of the number is:",reverse) 
