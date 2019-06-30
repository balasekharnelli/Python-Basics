#Create a for loop that prompts the user for 
# a hobby 3 times, then appends each one to hobbies.

hobbies = []
hobbies_count = 3

for hobby in range(0, hobbies_count):
    value = input("Enter your hobby: ")
    hobbies.append(value)
print(hobbies)
