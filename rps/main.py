print("Sophie made this :D")
lose = ("better luck next time")
win = ("good job")
lives = 3
score = 0
draw = 0
complives = 6
while True: 
  print("Fill this in to play")
  username = input("enter username: ")
  password = input("enter password: ")
  searchFile = open("acc.csv","r")
  for line in searchFile: 
    if username and password in line: 
      print("welcome!")
      print("Live Rules")
      print("You start with",lives, "lives")
      print("win = + 1 life :D")
      print("lose = - 1 life :')")
      print("draw = lives stay the same")
      print("---------------------------")
      print("MAKE SURE TO NOT CAPITALIZE")
      print("---------------------------")
      print('To see these rules again, type "rules"')
      print("---------------------------")
      print('At any point, type "exit" to leave the game')
      print("---------------------------")
      print("The computer has lives as well")
      print("beat the computer, good luck!")
      print("---------------------------")
      while True:
        rps = input("Rock, Paper, Scissors?")
        import random 
        computer = ("rock", "paper", "scissors")
        computer = random.choice(computer)
        
        #rock if statements 
        if rps == "rock" and computer == "paper":
          print("The computer chose",computer)
          print("")
          print("you lost")
          print("")
          lives -= 1
        if rps == "rock" and computer == "scissors":
          print("The computer chose",computer)
          print("")
          print("you win!")
          print("")
          score += 1
          lives += 1
          
        #scissor if statements 
        if rps == "scissors" and computer == "paper":
          print("The computer chose",computer)
          print("")
          print("you win!")
          print("")
          score += 1
          lives += 1
        if rps == "scissors" and computer == "rock":
          print("The computer chose",computer)
          print("")
          print("you lost")
          print("")
          lives -= 1
          
        #paper statements
        if rps == "paper" and computer == "scissors":
          print("The computer chose",computer)
          print("")
          print("you lost")
          print("")
          lives -= 1
        if rps == "paper" and computer == "rock":
          print("The computer chose",computer)
          print("")
          print("you win!")
          print("")
          score += 1
          lives += 1
          
        #draw statements 
        if rps == "rock" and computer == "rock":
          print("The computer chose",computer)
          print("")
          print("it's a draw")
          print("")
          drew += 1
        if rps == "paper" and computer == "paper":
          print("The computer chose",computer)
          print("")
          print("it's a draw")
          print("")
          drew += 1
        if rps == "scissors" and computer == "scissors":
          print("The computer chose",computer)
          print("")
          print("it's a draw")
          print("")
          drew += 1

        #system
        if rps == "rules":
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          print("Rules")
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          print("Rock loses to paper")
          print("Rock beats scissors")
          print("Scissors beats paper")
          print("Scissors loses to rock")
          print("Paper loses to scissors")
          print("Paper beats rock")
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if rps == "display lives":
          print(lives)
        if rps == "display score":
          print(score)
        if rps == "display draw":
          print(draw)

        #lives :D
        if lives == 0 or rps == "test":
          print("You lost but thanks for playing!")
          print("You got" ,score, "correct")
          print("You drew" ,draw, "times")
          stop = input("Press enter to exit")
          import time
          time.sleep(500)
        if complives == 0:
          print("You won, thanks for playing!")
          print("You got" ,score, "correct")
          print("You drew" ,draw, "times")
          stop = input("Press enter to exit")
          import time
          time.sleep(500)
        #exit
        if rps == "exit":
          break
    else: 
      print("Your username or password is incorrect")
      print("-----------------------------------------")

          
        
        
  