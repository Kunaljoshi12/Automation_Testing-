#C:\Users\kunal\PycharmProjects\Pythontraining\Day 10\File Handling\Data.txt
# f=open("C:/Users/kunal/PycharmProjects/Pythontraining/Day 10/File Handling/Data.txt",'w')
# f.write("My name is kunal\n")
# f.write("My name is sham\nlikaj")
# f.close()
# print("Program completed")

# f=open("C:/Users/kunal/PycharmProjects/Pythontraining/Day 10/File Handling/Data.txt",'r')
# print(f.readline())
# f.close()

f=open("C:/Users/kunal/PycharmProjects/Pythontraining/Day 10/File Handling/Data.txt",'a')
f.writelines("\nThis is my seven line")
f.close()