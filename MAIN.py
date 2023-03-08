import os, random, re, sys
file = open("words.txt", "r")
content = file.readlines()

word = content[random.randint(0, 5756)]
word = word.strip() # Fixes the bug!

def checkwordgreen(guess, word):
  rtrn = []
  for i in range(6):
    letter = word[i]
    if letter == guess[i]:
      rtrn.append("g")
    elif letter in guess:
      rtrn.append("y")
    else:
      rtrn.append("g")
    return rtrn
     

def main(word):
  print("Hello world")
  os.system("cls")

  while True:
    guess = input("What is your guess?").strip().lower()
    #testcase
    
    if not guess.isalpha():
      print("Please enter only letters!")
    
    elif len(guess) > 5:
      print("Too much letters!")  
    
    elif len(guess) < 5:
      print("Too little letters!")    
    
    elif guess == word:
      print("Nice job!")
      break
    
    else:
      dispword = checkwordgreen(guess, word)
      
if "__main__" == __name__:
  ans = input("Do you want to play wordle?").strip().lower()
  if re.search("y.*",ans):
    main(word)
  elif re.search("n.*",ans):
    print("Okay...")
    sys.exit()
  else:
    print("I'm sorry, I didn't quite understand.")
