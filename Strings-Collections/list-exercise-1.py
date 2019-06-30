list1 = input("Enter list of elements: ")
#^ Input method convertd everything into strings.
list1 = list1.split(",") 
#^ Splitting the string based on comma
print(type(list1))
#^ Above is a list of strings because split function returns list
print(type(list1[1]))
#^ Type should be of string as we split the string based on comma
print(type(list1[0]))
#^ Type should be of string as we split the string based on comma
print(type(list1[2]))
#^ Type should be of string as we split the string based on comma


print(list1)
sum = 0

for element in list1:
    sum = sum + int(element)
#Converting string into int
print(sum)

