class person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        

name = input("enter name")
age = input("your age")


if name =="":
    print("please enter your name")
elif age == "":
    print("please enter your age")
        
    
    
p1 = person(name,age) 
print(p1.name)
print(p1.age)       
        
        