# 1
input_1 = input("Enter the Value: ")
for i in range(0, int(input_1)):
  print("String 1")

#2
input_2 = int(input("Enter the Value: "))
while int(input_2) != 0:
  print("I'm looping", input_2) 
  input_2 -= 1

#3 Write a program that generates a random number (0-10) and ask you to guess it.
from random import randint
random_number = randint(1, 10)

guesses_left = 3
while guesses_left > 0:
  guess=int(input("Enter your number: "))
  if guess == random_number:
    print("You won")
    break
  guesses_left -= 1
else:
  print("You lose")

