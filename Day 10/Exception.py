# print("This is staring point of program...")
# print("This is staring point of program...")
# print("This is staring point of program...")
# try:
#     print(x)
# except:
#     print("This is end point of program...")
#     print("This is end point of program...")
#     print("This is end point of program...")


# print("Execution start")
# try:
#     print(10/0)
# except ZeroDivisionError:
#      print("Execution stop")
# print("Program is completed")
#

#Example 3 Multiple Except block try, except else, finally
# num1,num2=19,0
# try:
#     print(num1/num2)
#     exec("x === 5")  # invalid syntax
# except ZeroDivisionError:
#     print("Throw exception")
# except SyntaxError as e:
#     print("Caught:", e)
# else:
#     print("No exception")
# finally:
#     print("always executs...")
#
#
#
# try:
#     exec ("x === 5")  # invalid syntax
# except SyntaxError as e:
#     print("Caught:", e)
# else:
#     print("No exception")
# finally:
#     print("always run")


#Example4: raising our own exception
# def enterage(num):
#     if num<0:
#         raise ValueError("Only Integers are allowed")
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# num=1
# try:
#     enterage(num)
# except ValueError:
#     print("Exception occure")
# else:
#     print("Program is stop")