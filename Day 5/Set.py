# set1={"orange", 12, 45.35}
# print(set1)
from os import remove

set2={"apple","banana","cherry"}
# print(set2)

# set3={12, 45.35,7938,383}
# print(set3)

#Ex access index from set

# for i in set2:
#     print(i)

#Ex3 value exists ins et or not
# if "apple" in set2:
#     print("Yes")
# else:
#     print("No")

#Ex value is exist in set or not
# myset={"apple","banana","cherry"}
# print("banana" in myset)
# print("banana2" in myset)

#Ex adding items to set
#add()-add single item update()-add multiple items
myset={"apple","banana","cherry"}
# myset.add("orange")
# print(myset)
myset.update(["mango","grapes"])
print(myset)
#
# #Ex find number of items in set
# print(len(myset))

# Ex remove item from set
#
# myset.remove("mango")
# print(myset)

# myset.discard("grapes")
# print(myset)

# myset.discard("banana")
# print(myset)
# myset.remove("apple")
# print(myset)

#Ex: clear all items from set
# myset.clear()
# print(myset)

# del myset delete set
# print(myset)

#Ex joining 2 sets
set1={"1","2","3","4"}
# s=set1.union(set2)
# print(s)
#

set1.update("a","b","c","d")
print(set1)