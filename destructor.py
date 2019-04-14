class student:
    def __init__(self):
        print("constructor is being called!!")
    def __del__(self):
        print("destructor is being called!!")
        
s1=student()
del s1 
