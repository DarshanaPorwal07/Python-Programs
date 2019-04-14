list=[11,33,44,56,23,22]
print("Original list:")
print(list)
for i in list:
	if(i%2 == 0):
	    list.remove(i)

print("list after removing EVEN numbers:")
print(list)
