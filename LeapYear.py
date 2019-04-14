year=int(input("enter the year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("this is leap year!")
else:
    print("not a leap year")
