c = 5

while c != 0:
    print(c)
    c -= 1

while c:       # It works because c will be 0 after 5 iterations & expression will be false
    print(c)
    c = -1

#Infinite Loop

#while True:
#    print("Looping!")


#Break
while True:
    response = input() #Note
    if int(response) % 7 == 0:
        break
