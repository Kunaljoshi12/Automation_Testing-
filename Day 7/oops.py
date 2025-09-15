# class Myclass:
#     def myfunction(self):
#         pass
#     def display(self):
#         print("kunal")
# m=Myclass()  #objects
# m.myfunction()
# m.display()

#Ex: 2
# class Myclass:
#     def m1(self):
#         pass
#     @staticmethod
#     def m2(self,num):
#         print(num)
#
# m=Myclass()
# m.m1()
# Myclass.m2(45,12)

# class Addition:
#     def add(self,a,b):
#         return a+b
#     @staticmethod
#     def add(self,a,b):
#         print( a+b)
# m=Addition.add(34,12,34)
# print(type(m))
# Addition.add(1, 34, 345)
#
#

#EX: variable

# class Addition:
#     a,b=12,56
#     def add(self):
#         print(self.a+self.b)
#
#     def mul(self):
#         print(self.a * self.b)
# m=Addition()
# m.add()
# m.mul()

#Ex: 4
# i,j=12,45 #Globle variables
# class Myclass:
#     a,b=12,48 #Class variables
#     def add(self,x,y):  #local variables
#         print(x+y)#local variables
#         print(self.a+self.b)#Class variables
#         print(i+j)#Globle variables
# m=Myclass()
# m.add(1,33)


#EX:
# a,b=12,45 #Globle variables
# class Myclass:
#     a,b=12,48 #Class variables
#     def add(self,a,b):  #local variables
#         print(a+b)#local variables
#         print(self.a+self.b)#Class variables
#         print(globals()['a']+globals()['b'])#Globle variables
# m=Myclass()
# m.add(1,33)

#Ex Once class multiple objects
# class Myclass:
#     @staticmethod
#     def display(self,n):
#         print("This is firts name",n)
#     def display(self,name):
#         print("This is firts name",name)
# Myclass().display("Ghanshyam")
# Myclass().display("Alpana")
# m1=Myclass()
# m2=Myclass()
# m1.display("Kunal")
# m2.display("Shriya")

#Ex: constructor
class Myclass:
    def __int__(self):
        print("this is contructor ")
    def m1(self):
        print("hello...")
    def m2(self,x,y):
        return (x+y)
m=Myclass() # invke cnstructor automatically
m.m1() #method we have excipitely by using object
v=m.m2(21,23)
print(v)