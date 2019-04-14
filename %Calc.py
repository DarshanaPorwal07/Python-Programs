total=int(input("enter the total marks:"))
sub1=int(input("enter the marks of 1st subject:"))
sub2=int(input("enter the marks of 2ns subject:"))
sub3=int(input("enter the marks of 3rd subject:"))
sub4=int(input("enter the marks of 4th subject:"))
sub5=int(input("enter the marks of 5th subject:"))

marks_obtained=sub1+sub2+sub3+sub4+sub5

print("---------------------------------------------")
print("Total marks obtained is: ",marks_obtained)
percentage=(marks_obtained/total)*100
print("Percentage is :",percentage)
