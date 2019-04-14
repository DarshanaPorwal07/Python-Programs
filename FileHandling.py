f = open("d:/myfile.txt", "x")

f.close()
f=open("d:/myfile.txt","w")
print(f.write(input("enter the text")))
f.close()
f = open("d:/myfile.txt", "r")
print(f.read())
f.close()
f = open("d:/myfile.txt", "x")

f.close()
