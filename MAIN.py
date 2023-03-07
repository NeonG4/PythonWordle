import os, random
def Main():
  file = open("words.txt", "r")
  word = readline(random.randint(0, 5756))
  print("Hello world")
  os.system("clear")
  while True:
    guess = input("What is your guess?")
    #testcase
    if guess == word:
      print("Nice job!")
    else:
      print("Try again...")
      
if "__name__" == __main__:
  Main()
