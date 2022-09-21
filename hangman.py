#                                  HANGMAN
# -------------------------------------------------------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return wordlist
    


def choose_word(wordlist):
    
    return random.choice(wordlist)



wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  
  res = 0
  for i in secret_word:
    if i in letters_guessed:
      res += 1
  if res == len(secret_word):
    print(True)
  else:
    print(False)
secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']




def get_guessed_word(secret_word, letters_guessed):
  res = ''
  for i in secret_word:
    if i in letters_guessed:
      res += i
    else:
      res += '_'
  return res
      

def get_available_letters(letters_guessed):
  res = string.ascii_lowercase
  for i in res:
    if i in letters_guessed:
      res = res.replace(i,"")
  return res
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']

def hangman(secret_word):
  intro = str(len(secret_word))
  lettersGuessed = []
  guess = str
  mistakesMade = 6
  wordGuessed = False
  mistake = 3
    
  print ('Welcome to the game, Hangman!')
  print ('I am thinking of a word that is ', intro,' letters long.')
  print ('------------')

  while mistakesMade > 0 and mistakesMade <= 6 and wordGuessed is False:
      if secret_word == get_guessed_word(secret_word, lettersGuessed):
          wordGuessed = True
          break
      print ('You have ', str(mistakesMade), ' guesses left.')
      print ('Available letters: ', get_available_letters(lettersGuessed))
      guess = input('Please guess a letter: ').lower()

      if guess in secret_word:
          if guess in lettersGuessed:
              print ("Oops! You've already guessed that letter: ", get_guessed_word(secret_word, lettersGuessed))
              print ('--------')
              
          else:
              lettersGuessed.append(guess)
              print ('Good guess: ',get_guessed_word(secret_word, lettersGuessed))
              print ('--------')

      if guess not in get_available_letters(lettersGuessed):
        mistake -= 1
        if mistake < 0:
          mistakesMade -= 1
        if mistake >= 0:
          print('You have',mistake,'warning')
          print('Write only the letters')        
      else:
          if guess in lettersGuessed:
              print ("Oops! You've already guessed that letter: ", get_guessed_word(secret_word, lettersGuessed))
              print ('--------')
              
          else:
              lettersGuessed.append(guess)
              mistakesMade -= 1
              print ('Oops! That letter is not in my word: ', get_guessed_word(secret_word, lettersGuessed))
              print ('--------')
       
              

  if wordGuessed == True:
      return 'Congratulations, you won!'
  elif mistakesMade == 0:
      print ('Sorry, you ran out of guesses. The word was ')





def match_with_gaps(my_word, other_word):

  my_word_stripped = my_word.replace(" ", "")
  same_char = list()
  blank_stripped = list()
  if len(my_word_stripped) == len(other_word):
      for index, letter in enumerate(my_word_stripped):
          if letter in string.ascii_lowercase:
              same_char.append(index)
          else:
              blank_stripped.append(index)
            
  else:
      return False

  mws = ''
  ow = ''
  for index_same in same_char:
      for index_dif in blank_stripped:
          if other_word[index_dif] == other_word[index_same]:
              return False
          else:
              mws += my_word_stripped[index_same]
              ow += other_word[index_same]
    
  if mws == ow:
      return True
  else:
      return False
   



def show_possible_matches(my_word):
  possible_matches = list()
  for i in wordlist:
      if match_with_gaps(my_word, i):
          possible_matches.append(i)
    
  spm = ' '.join(possible_matches)
    
  return spm
    



def hangman_with_hints(secret_word):
  secret_word = choose_word(wordlist)
  letters_guessed = list()
  warnings_remaining = 3
  guesses_remaining = 6
  good_guess = 0
  print('''
        \n
        OOO-----------------------------------------------OOO
        \n
                        Welcome to the Hangman+!,
                       
                       
            I'm thinking of a word that is %d letters long.
        \n
        OOO-----------------------------------------------OOO
        \n
        ''' % len(secret_word))
          
          
  while not is_word_guessed(secret_word, letters_guessed) and guesses_remaining > 0:
        
      print("\nYou have %d guesses left." % guesses_remaining)
      get_available_letters(letters_guessed)
      letter = str.lower(input("Please guess a letter: "))
        
      if letter == '*':
          print("Possible matches are:", show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        
      elif not letter or letter not in string.ascii_lowercase:
          if warnings_remaining != 0:
              warnings_remaining -= 1
              print("That is not a valid letter. You have %d warning left." % warnings_remaining)
          else:
              print("That is not a valid letter. You have no warning left, so you lose one guess.")
              guesses_remaining -= 1

      elif letter in letters_guessed:
          if warnings_remaining != 0:
              warnings_remaining -= 1
              print("You've already guessed that letter. You have %d warning left." % warnings_remaining)
          else:
              print("You've already guessed that letter. You have no warning left, so you lose one guess.")
              guesses_remaining -= 1
        
      else:
          letters_guessed.append(letter)
          if letter not in secret_word:
              print("That letter is not in my word.")
              if letter in 'aiueo':
                  guesses_remaining -= 2
              else:
                  guesses_remaining -= 1
          else:
              print("Good guess!")
              good_guess += 1 
                
      print(get_guessed_word(secret_word, letters_guessed)) 
      print("\nOOO-----------------------------------------------------------------------OOO\n")
        
      if is_word_guessed(secret_word, letters_guessed):
          print("Congratulations, you won!")
          print("Your total score for this game is %d." % (good_guess * guesses_remaining))
        
      if guesses_remaining == 0:
          print("Sorry, you ran out of guesses. The word was %s." % secret_word)
    


if __name__ == "__main__":
    pass

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
