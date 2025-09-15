#Ex1 create list
# mylist1=[12,323,212,12,342]
# mylist2=["apple","banana","cherry"]
# mylist3=["apple","banna",23,12.3]
# mylist4=list()
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist4)

#Ex2 accessing item from lit
# mylist=["apple","banana","cherry"]
# print(mylist[0:2])

#Ex3 Range of index
#mylist=["apple","banana","cherry","mango","orange","apple", "banana"]
# print(mylist[-2:-1])
# print(mylist[0:2],mylist[3:5])
# l1=mylist[0:2]
# l2=mylist[-2:]
# print(l1<=l2)
# l3=l1+l2
# print(l3)

#Ex4  change item values
# mylist=["apple","banana","cherry"]
# print(mylist)
# mylist[0]="cherry"
# mylist[2]="apple"
# print(mylist)

#Ex5 read the items using list
# mylist=["apple","banana","cherry"]
# for i in mylist:
#     print(i)

#Ex6 check the item is inlist or not
# mylist=["apple","banana","cherry"]
# if "apple" in mylist:
#     print("Yes")
# else:
#     print("No")

#Ex7 list length
# mylist=["apple","banana","cherry"]
# print(len(mylist))

#Ex8 add item append() insert()
#mylist=["apple","banana","cherry"]
# # mylist.append("orange")
# # print(mylist)
# mylist.insert(2,"watermelon")
# print(mylist)

#Ex9 remove item from list
# mylist=["apple","banana","cherry"]
# mylist.remove("apple")
# mylist.pop(0)
# print(mylist)

#Ex10 del
# mylist=["apple","banana","cherry"]
# del mylist[0]
# print(mylist)

#Ex11 clear
# mylist=["apple","banana","cherry"]
# mylist.clear()
# print(mylist)

#Ex copy list
mylist1=["apple","banana","cherry"]
mylist2=["apple","banana","cherry"]
# mylist2=list(mylist1)
# print(mylist1  )
# print(mylist2 )

#copy
# mylist2=mylist1.copy()
# print(mylist2)

#Ex joining list
# list3=mylist1+mylist2
# print(list3)

#Ex join list using loop

# for i in mylist2:
#     mylist1.append(i)
# print(mylist1)

#using extend()
# list1=['12','d','34']
# list2=[12,4,5,3,2,'a']
# list1.extend(list2)
# print(list1)