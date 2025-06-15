# Number Guess Game
import random

def guess_check():
  guess_number = random.randint(1,100)
  trying_count = 0

  while True :
    try :
      guess = int(input("Guess the Number from 1 - 100 : "))
      trying_count += 1
      
      if guess < 1 or guess > 100 :
        print('Please guess a number between 1 and 100!')
      else :
        if guess < guess_number:
          print('Too low!')
        elif guess > guess_number:
          print('Too high!')
        else:
          print("Congratulations you win!!")
          print(f'You guessed successfully in {trying_count} tries')
          break
      
    except ValueError:
      print("Please enter a valid number")
      
def main():
  while True:
    guess_check()
    again = input('Again [Y/n]? ').lower()
    if again == 'n' :
      print('Exit Program...')
      break
    elif again == 'y' :
      print('Running Program again..')
    else :
      print('Invalid Input!')
      print('Forced Program Exit..')
      break
      
if __name__ == '__main__' :
  main()