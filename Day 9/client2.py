#Approch 1
# import sys
# sys.path.append("C:/Users/kunal/PycharmProjects/Pythontraining/Day 9/Pack1")
# sys.path.append("C:/Users/kunal/PycharmProjects/Pythontraining/Day 9/Pack1/Pack2")
#
# import module1
# import module2
#
# module1.display()
# module2.show()

#Approch 2
import sys
sys.path.append("C:/Users/kunal/PycharmProjects/Pythontraining/Day 9/Pack1")
sys.path.append("C:/Users/kunal/PycharmProjects/Pythontraining/Day 9/Pack1/Pack2")

from module1 import *
from module2 import *

display()
show()