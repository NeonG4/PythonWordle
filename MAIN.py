import os, random, re, sys
file = open("words.txt", "r")
word = readline(random.randint(0, 5756))


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
  os.system("clear")
  while True:
    guess = input("What is your guess?")
    #testcase
    if guess == word:
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
