# v,c,x,z="a",'a',"ncuus",'bssds'
# print(v,c,z,x)
#
# s=str("Welcome")
# # print(s)
#
# n=str()
# print(type(n))
# n,v,t="kunal",12,21.34
# print(n,v,t)

#mutable, immutable

# str="Welcome"
# print(id(str))
#
# str=str+"to python"
# print(id(str))

#Ex + and * with string
# str="Welcome"
# print(str+"programming") # concatination
#
# print(str*2) #string printed 2 times

#Ex slicing []
# str="Welcome"
# print(str[1:6])

# str1,str2="Kunal","Joshi"
# print(str1[4:5]+str2[4:5])
# print((str1[4:5]+str2[4:5])*2)
# print(str1[4:5]+str2[4:5]*2)
# print((str1[4:5])+str2[4:5]*2)
# print((str1[0:1]+str2[0:1])*2)
# print(str1[0:-4])

#Ex: ord() & chr()
# print(ord('A'))
# str="Help"
# print(ord(str[0:1]))
# print(chr(68))


#Ex max() min() len()
#
# print(max("abc"))
# print(max(12,12,34,23))
# print(max('A','B','a','b '))
#
# print(min("abc"))
# print(min(12,12,34,23))
# print(min('A','B','a','b'))
#
# print(len("abc"))

#Ex  in or not in functions - returns true/false
# s="Welcome"
# print("come" in s)
# print("mncnnd" in s)
#
# print("come" not in s)
# print("mncnnd" not in s)

#Ex String comparison
# print("tin"=="tie")
# print("Free"!="True")
# print("arrow">"arro")
# print("arrow"<"arrroww")
# print("arrow"!="arro ")
# print("arrow"!="worra ")
# print()
#
#
# x=121232223
# y=123332231
# c=x
# x=y
# print(c,"",x)


#Ex Testing strings
# s="Welcome to python"
# print(s.isalnum())
# print("Welcome".isalpha())
# print("2012".isdigit())
# print("first number".isidentifier())
# print(s.islower())
# print("WELCOME".isupper())
# print(" ".isspace())

#Ex searching for substring
# s="Welcome to QK"
# print(s.endswith("QK"))
# print(s.find("K"))
# print(s.startswith("W"))
# print(s.count("e"))
# print(len(s))
# print(s.islower())
# print(s.isupper())

#Ex converting String
# s="String in PYTHON"
# s1=s.capitalize()
# print(s)
#
# s2=s.title()
# print(s2)
#
# s3=s.lower()
# print(s3)
#
# s4=s.replace("in", "on")
# print(s4)

#Ex reverse string
# s="Welcome"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str
# print("reversed string is:",rev_str)