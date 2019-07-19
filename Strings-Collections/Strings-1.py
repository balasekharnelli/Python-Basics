"""
Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""
MyList = ['abc', '1221', 'aba', 'f2f', 'aa', 'sd']

# for i in MyList:
#     if ( len(i) > 2 and i[0] == i[-1]):  #Important point
#         print(i)

for i in MyList:
    if len(i) > 2 and \
        i[0] == i[-1]: #We can define two conditions in if conditions in the both ways
        print(i)
