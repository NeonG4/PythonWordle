import os, random, sys, logging




def checkword(guess, word):
  rtrn = []
  for i in range(0, 5, 1): # we should change the 5 to be the length of the word
    letter = word[i]
    if letter == guess[i]:
      rtrn.append("🟩")
      logging.debug("green Letter")
    elif letter in guess:
      rtrn.append("🟨")
      logging.debug("yellow Letter")
    else:
      rtrn.append("⬜")
      logging.debug("white Letter")
  return rtrn


def main(word):
  logging.debug("Started func")
  cycles = 0

  while True:

    if cycles >= 6:
      print("Game over! You lost")
      logging.debug("Cycles >= 6")
      print("The word was " + word)
      break
    logging.debug("Getting guess")
    guess = input("What is your guess?").strip().lower()
    logging.debug("Got guess")
    # testcase

    if not guess.isalpha():
      print("Please enter only letters!")
      logging.debug("failed isalpha")

    elif len(guess) > 5:
      print("Too much letters!")
      logging.debug("failed lettercount1")
      

    elif len(guess) < 5:
      print("Too little letters!")
      logging.debug("failed lettercount2")
     

    elif not guess in content:
      print("Please enter an existing word!")
      logging.debug("failed trueword")

    elif guess == word:
      print("Nice job!")
      logging.debug("correct word")
      
      break

    else:
      cycles += 1
      logging.debug("Word passed checks")
      result = checkword(guess, word)
      
      for letter in result:
        print(letter, end="")
      print("")

if "__main__" == __name__:
  file = open("words.txt", "r")
  content = file.readlines()
  content = [s.lower().strip() for s in content]
  word = content[random.randint(0, 5756)]
  logging.basicConfig(filename="output.log",
                      filemode='w',
                      format='%(asctime)s,%(msecs)d %(levelname)s :: %(message)s',
                      datefmt='%H:%M:%S',
                      level=logging.DEBUG                    
                      )
  logging.debug("Correct Word:" + word)
  main(word)

