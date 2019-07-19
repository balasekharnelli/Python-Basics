MyList = [2, 10, 23, 43, 1, 9, 4, -12]

MinValue = MyList[0]

for element in range(1, len(MyList)):
    if MyList[element] < MinValue:
        MinValue = MyList[element]
print(MinValue)