from random import *
reached = False
r = randint(1,100)
while not reached:
    Guess_number = int(input("Guess a number between 1 and 100: "))
    if Guess_number <1 or Guess_number >100 :
       print("Your guess is outside range 1-100!")
    else:
      if Guess_number == r:
         print("Congratulation! You win.")
         reached = True
      elif Guess_number > r:
        print("Go lower")
      else:
        print("Go higher")