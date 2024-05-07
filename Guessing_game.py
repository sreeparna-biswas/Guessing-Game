import random
playerName=input("Hello, What's your name? ")
print()
print("Hi, "+playerName+" I am Guessing a number between 1 and 100:")
#print(f"Hi, {playerName} I am Guessing a number between 1 and 100:") #String Format
num=random.randint(1,100)
print()
guesses=input("Choose the difficulty Level, Type 'easy' or 'hard':")
print()
if guesses=='easy':
  number_of_guesses=10
  print("You have 10 attempts to guess the number.")
elif guesses=='hard':
  number_of_guesses=5
  print("You have 5 attempts to guess the number.")
#else part
c=0
number_of_guesses_cpy=number_of_guesses
print()

while(True):
  if c==number_of_guesses:
    print("Defeat! The correct number is: "+str(num))
    break
  else:
    guess_num=int(input("Make a guess:"))
    if guess_num>=1 and guess_num<=100:
      number_of_guesses_cpy=number_of_guesses_cpy-1
      c=c+1
      if guess_num==num:
        print("You got it!  The answer was "+str(guess_num)+".")
        print("You guessed the number in "+str(c)+" tries!")
        print()
        break
      elif guess_num>num:
        print("Your guess is too high")
        print("Guess again.")
        print("You have "+str(number_of_guesses_cpy)+" attempts to guess the number.")
        print()
      elif guess_num<num:
        print("Your guess is too low")
        print("Guess again.")
        print("You have "+str(number_of_guesses_cpy)+" attempts to guess the number.")
        print()
    else:
      print()
      print("Wrong Input!!Guess Again between 1 to 100:")
      print()
