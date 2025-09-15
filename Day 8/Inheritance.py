#single
# class A:
#     def m1(self):
#         print("This is M1")
#
# class B(A):
#     def m2(self):
#         print("This is M2")
#
# obj=B()
# obj.m1()
# obj.m2()
from encodings import search_function
from symtable import Class

from jinja2.filters import do_last


#Multilevel
# class C:
#     x,v,z=23,45,56
#     def m1(self):
#         print(self.x,self.v,self.z)
#
# class D(C):
#     def m2(self):
#         print(self.x+self.v+self.z)
#
# class E(D):
#     def m3(self):
#         print(self.x-self.v-self.z)
#
# class F(E):
#     def m4(self):
#         print(self.x*self.v*self.z)
#
# obj=F()
# obj.m1()
# obj.m2()
# obj.m3()
# obj.m4()

#Multiple
# class G:
#     def m5(self):
#         for i in range(1,11):
#             print(i)
# class H:
#     def m6(self):
#         for i in range(11,21):
#             print(i)
# class I(G,H):
#     def m7(self):
#         print("Execution is done")
#
# obj=I()
# obj.m5()
# obj.m6()
# obj.m7()

#Herachy
# class J:
#     x,y=120,34
#     def m1(self):
#         print(self.x+self.y)
#
#
# class K(J):
#     c, l = 1204, 34
#
#     def m2(self):
#         print(self.c + self.l)
#
# class L(J):
#     c, l = 1230, 34
#
#     def m3(self):
#         print(self.c + self.l)
#
# obj1=K()
# obj2=L()
# obj1.m2()
# obj1.m1()
# obj2.m3()
# obj2.m1()

#Ex6
# class A:
#      def m1(self):
#          print("This is class A")
# class B(A):
#     def m1(self):
#         print("This is class B")
#
# obj=A()
# obj.m1()
#
# obj=B()
# obj.m1()

#Ex7
# class A:
#     a,b=12,56
#
# class B(A):
#     i,j=24,56
#     def m(self,x,y):
#         print("Local variable output: ",x+y, "Class variable of A output: "
#               ,self.a+self.b, "Class variable of A output:",self.i+self.j)
# obj=B()
# obj.m(56,89)

#Variable overriding
# class A:
#     a,b=12,56
#
# class B(A):
#     a,b=24,56
#     def m(self,a,b):
#         print("Local variable output: ",a+b, "Class variable of A output: "
#               ,self.a+self.b, "Class variable of A output:",self.a+self.b)
# obj=B()
# obj.m(56,89)

#Ex Variable overriding
# class A:
#     name="Kunal"
#
# class B(A):
#     name = "Sham"
#     def call(self):
#         print(super().name)
#
#
# class C(B):
#     name = "Shiva"
#     def test(self):
#         print(super().name)
#
# c=C()
# print(c.name)
# c.test()
# c.call()

# class A:
#     name = "Kunal"
#     def n(self):
#         print("Class A name:", A.name)
#
#
# class B:
#     name = "Joshi"
#     def n(self):
#         print("Class B name:", B.name)
#
#
# class C(A, B):
#     def display(self):
#         A.n(self)   # Call Class A's method
#         B.n(self)   # Call Class B's method
#
#
# c = C()
# c.display()

#Ex overloading
class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("Hello" +name)
        else:
            print("Hello")

h=Human()
h.sayhello(" Kunal")
h.sayhello()