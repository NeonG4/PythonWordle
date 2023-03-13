import os, random, re, sys, subprocess, logging

file = open("words.txt", "r")
content = file.readlines()
content = [s.strip() for s in content]

word = content[random.randint(0, 5756)]
word = word


def checkword(guess, word):
  rtrn = []
  for i in range(0, 5, 1):
    letter = word[i]
    if letter == guess[i]:
      rtrn.append("🟩")
    elif letter in guess:
      rtrn.append("🟨")
    else:
      rtrn.append("⬜")
  return rtrn


def main(word):
  logging.debug("Started func")
  os.system("cls")
  os.system("clear")
  cycles = 0

  while True:

    if cycles >= 6:
      print("Game over! You lost")
      logging.debug("Cycles >= 6")
      break
    logging.debug("Getting guess")
    guess = input("What is your guess?").strip().lower()
    logging.debug("Got guess")
    #testcase

    if not guess.isalpha():
      print("Please enter only letters!")
      logging.debug("failed is alpha")

    elif len(guess) > 5:
      print("Too much letters!")

    elif len(guess) < 5:
      print("Too little letters!")

    elif not guess in content:
      print("Please enter an existing word!")

    elif guess == word:
      print("Nice job!")
      break

    else:
      cycles += 1
      result = checkword(guess, word)
      print(result)


if "__main__" == __name__:
  ans = input("Do you want to play wordle?").strip().lower()
  if re.search("y.*", ans):
    main(word)
  elif re.search("n.*", ans):
    print("Okay...")
    sys.exit()
  else:
    print("I'm sorry, I didn't quite understand.")
