i = 10
print(isinstance(i, int))
# True
#isinstance method returns bool values, either True or False
#print(isinstance(i, list))
# False
#=================================

MyList = input("Enter the list of number: ")
MyList = MyList.split(",")

Mul = 1

for element in MyList:
    Mul = Mul * int(element)

print(Mul)