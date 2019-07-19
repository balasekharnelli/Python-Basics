MyList = [2, 10, 23, 43, 1, 9, 4]

#Initialise
MaxValue = MyList[0]
for element in range(1, len(MyList)):
    if MyList[element] > MaxValue:
        MaxValue = MyList[element]
print(MaxValue)