def guessing_game(my_number, max_guesses):
  print('I\'m thinking of a number can you guess it')
  print(f'You can have up to {max_guesses} guesses')
  print('you will be given a hint after each guess stating whether you guessed too high or too low')

  guesses=0
  previous_guess=0

  while guesses!=max_guesses:

    guess=get_valid_guess()

    if guess!=previous_guess:
      
      previous_guess=guess
      guesses+=1

      if guess<my_number:
        print('Too Low')
      elif guess>my_number:
        print('Too high')
      elif guess==my_number:
        print(f'You guessed it!! :) my number was {my_number} it only took you {guesses} tries')
        break
        
        
      print(f'You have taken {guesses} guesses so far')
      if guesses==max_guesses:
        print(f'you used up all the guesses')
        print(f'you lost the game :( my number was {my_number} ')
        
      

    else:
      print(f'you already guessed {guess} it wasnt right, guess again')


def get_valid_guess():
  while True:
    guess=input('Please enter your guess: ')
    if guess.isnumeric():
      guess=int(guess)
      return guess
    else:
      print('please enter a valid guess')
      continue 
  


guessing_game(my_number=10,max_guesses=4)
