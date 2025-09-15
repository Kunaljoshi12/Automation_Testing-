#Ex:
# class Myclass:
#     name='Kunal'
#     def __init__(self,name):
#         print(self.name)
#         print(name)
# Myclass("Shriya")

#Ex:
# class Myclass:
#     def __init__(self,id,name,sal):
#         self.id,self.name,self.sal=id,name,sal
#     def display(self):
#         print( self.id,self.name,self.sal)
# m=Myclass(102,"Kunal",27000)
# m.display()
#
# v=Myclass(105,"Shriya",67889)
# v.display()

# class Emp:
#     def __init__(self, id, name, sal):
#        self.id,self.name,self.sal=id,name,sal
#     def __str__(self):
#       return(self.name,self.sal)
# e=Emp(101,"kunal",5000)
# print(e)


# class Emp:
#     def __init__(self, id, name, sal):
#         self.id, self.name, self.sal = id, name, sal
#
#     def __str__(self):
#         return f"Name: {self.name}, Salary: {self.sal}"
#
#
#
# e = Emp(101, "Kunal", 5000)
# print(e)

# class Emp:
#     def __init__(self, id, name, sal):
#         self.id, self.name, self.sal = id, name, sal
#
#     def __str__(self):
#         return f"Employee[ID= {self.id}, Name= {self.name}, Salary= {self.sal}]"
#
# e = Emp(101, "Kunal", 5000)
# print(e)

class A:
    def __init__(self, a, b):
        self.a, self.b = a, b

class B(A):
    def __init__(self, *args, n, v):
        super().__init__(*args)   # passes (a,b) directly
        self.n, self.v = n, v

    def display(self):
        print(self.a + self.b)
        print(self.n + self.v)

m = B(10, 20, n=30, v=40)
m.display()

