def push(a,n):
    if len(list)>n:
        print("can't append,stack is full0")
    else:    
        list.append(a)
        print(list)
def pop():
    if len(list)==0:
        print("list is empty")
    else:
        print(list.pop())
        return list

n=10
list=["pqr","abc","xyz"]
choice=input("enter choice :1 for push and 2 for pop:")
if choice==1:
    element=input("enter the element")
    push(element,n)
else:
    pop()
