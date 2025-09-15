#Ex1
# mytuple=("banana","orange","mango",12.4)
# print(mytuple)
from Day4.List import mylist1

#Ex2 access tuple items
# mytuple=("banana","orange","mango",12.4)
# print(mytuple[0:2],mytuple[-2:0])

#ex change tuple value
#convert tule>>list(modify)>>tuple
# mytuple=("banana","orange","mango",12.4)
# mylist=list(mytuple)
# mylist.append("apple")
# v=tuple(mylist)
# print(v)

# mytuple1=("banana","orange","mango",12.4)
# mytuple2=("banana","orange","mango",12.4)
# mylist1=list(mytuple1)
# mylist2=list(mytuple2)
# v=mylist1+mylist2
# mytuple=tuple(v)
# print(mytuple)

# mytuple=("orange",12,45.35)
# mylist=list(mytuple)
# mylist[2]=4464
# t=tuple(mylist)
# print(t)

mytuple = ("orange", 12, 45.35)
# for i  in mytuple:
#     print(i)

# if 12 in mytuple:
#     print("yes")
# else:
#     print("no")

print(len(mytuple))

del mytuple
print(mytuple)