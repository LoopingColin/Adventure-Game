import random
import time

#def of functions

# make sure you play the game multiple times to win 
# change value of dragondead=false and legendarysword=false to true at the bottom of page for different results

def start():
  print("")
  print("Welcome to your adventure, "+ name +" The story will present you with different choices on what to do")
  print("")
  print("Your name is "+name+", and you're an adventurer who is trying to make a name for themselves")
  pickSide()

def pickSide(): 
  print("")
  answerSide = input("Which path do you take to go to the dungeon? (right or left)").lower()
  if (answerSide == "right" or answerSide == "r")  :
    goRight()
  elif (answerSide== "left" or answerSide == "l"):
    print("")
    print("You decide to go left and a goblin blocks your path")
    goLeft()
  else:
    print("Invalid answer. Why don't you try again?")
    pickSide()


def goRight():
  if DragonDead == False:  
    print("You shouldn't go here fool that enemy is too strong for an E rank adventurer you need to be A or higher.")
    pickSide()
  else:
    print("You see a sign that says:\"The Griffin has been slain by S rank Adventurers and we can finally get ready to head to the dungeon.\"")
    answer = input("Do you want to stop to get some food and supplies first at the blacksmith?").lower()
    if answer == "yes" or answer == "y" or answer == "blacksmith" or answer == "go to the blacksmith":
      print("You continue down the road and soon reach a small town, and do you want to  visit the blacksmith Ruok to get supplies and food.")
      blacksmith()
    elif answer == "no" or answer == "n":
      pickSide()
    else:
      print("Invalid answer. Why don't you try again?")
      goRight()
     
def blacksmith():
  answer = input("Do you go visit the blacksmith or do you continue on your journey to a dungeon?")


def goLeft(): #see dungeon
  print("")
  answerDungeon = input("Do you enter the dungeon or do you prepare first? (dungeon/prepare first)").lower() 
  if answerDungeon == "enter" or answerDungeon == "dungeon" or answerDungeon == "enter dungeon":
    print("")
    print("You gather all of your courage and enter the dungeon. You use a magic spell to light the dungeon \n You begin to walk until you reach the first floor of the dungeon where you encounter slime monsters.")
    enterDungeon()
  elif answerDungeon == "prepare" or answerDungeon == "prepare first" or answerDungeon == "wait":
    leaveDungeon()
  else:
     print("Invalid answer. Why don't you try again?")
     goLeft()
    


    
def enterDungeon(): # see statue
  print("")
  answerStatue = input("Do you check the statue after defeating the slime's or do you leave for the day (check/leave)").lower()
  if answerStatue == "check" or answerStatue == "statue" or answerStatue == "check statue":
    print("")
    print("You approach the statue to examine it. You activate the statue then An Orc appears ")
    checkStatue()
  elif answerStatue == "leave" or answerStatue == "leave dungeon":
    print("Suspecting The statue may be a trap you leave to recollect your thoughts until the next adventure")
    leaveDungeon()
  else:
     print("Invalid answer. Why don't you try again?")
     enterDungeon()

def checkStatue(): # see monster
  print("")
  answerCheckStatue = input("Do you fight or run? (fight/run)").lower()
  if answerCheckStatue == "fight":
    print("")
    print("You decide to try your luck fighting the orc, but your old sword gets parried by the monster and you are unable to grab it while it comes charging at you.\nThe beast attacks you sending you back to the wall, and you try to escape.\nHowever, you're too late. Then the orc eats you leaving no trace.")
    gameOver()
  elif answerCheckStatue == "Run":
    print("")
    print("You dodge the monster's attack. Then you safely run out of the dungeon.")
    leaveDungeon()
  elif answerCheckStatue == "freeze":
    winMonster()
  else:
    print("Invalid answer. Why don't you try again?")
    checkStatue()
    
def winMonster(): #defeats monster
  global legendarySword
  print("")
  print("Shaking in your boots you stand there afraid, the monster eats your right arm then falls asleep")
  print("Behind the sleeping monster, you see an old chest. You open it and see a legendary sword:\"Dragon Slayer\". It looks incredible.")
  legendarySword = True
  leaveDungeon()
  
def leaveDungeon(): 
  time.sleep(1)
  print("")
  print("You continue your adventure and arrive at a broken bridge above a river. On the other side you see a woman and bandits trying to steal from what looks like someone from royalty")
  bridge()

def bridge(): # see bridge
  answerBridge = input("Do you try to cross the bridge to help the woman or do you stay on this side and do nothing? (cross/stay)").lower()
  if answerBridge == "stay" or answerBridge == "don't jump" or answerBridge == "no":
    print("")
    print("The same Orc that was in the dungeon followed you and ends your life.")
    gameOver()
  elif answerBridge == "cross" or answerBridge == "cross bridge":
   print("")
   print("As you jump to the other side of the bridge, you use your magic abilities to cushion your fall.\nYou land on the other side of the bridge rushing to help the woman ")
   print("The woman thanks you and expalins that she was traveling to go find the legendary sword dragon slayer to fight the demon leader and defeat him to end the war.")
   print("He thinks in his mind that's the sword he took and doesn't tell her anything about it. She invites you to her home.")
   choices()
  else:
    print("Invalid answer. Why don't you try again?")
    bridge()
  
def choices():
  print("")
  Choice = input("Do you go to her home or do you head home? (her home/go home)").lower()
  if Choice == "her home" or Choice == "woman home" or Choice == "go to her home":
    print("")
    print("She takes you to visit her home after saving her from the bandits")
    print("While traveling down the road you encounter a dragon")
    dragon()
  elif Choice == "home" or Choice == "go home" or Choice == "head home":
    print("You've had enough of this adventure. You go home to sleep.\nPerhaps you'll try again tomorrow...")
    gameOver()
  else:
    print("Invalid answer. Why don't you try again?")
    choices()

def dragon():
  print("")
  global legendarySword
  if legendarySword == True:
    print("Your new sword is sharp and gives you the abilities of a hero, making you really strong and fast. As well as increasing your mp capacity making it so you can use multiple magic skills at a time")
  else:
    print("Your sword loses power not activating the hero's abilities making you have an even harder time for the fight.")
  attack()
  
def attack():
  global legendarySword
  if legendarySword == True:
    chance = 10
  else:
    chance = 2
  inp = input("You attack using fireball (attack)").lower()
  if inp == "attack":
    result = random.randint(2,chance)
    if result <= 2:
      winDragon()
    else:
      loseDragon()
  else:
    print("You fool kill the dragon before he burns you and the princess alive!")
    attack()
    

def winDragon():
  global DragonDead
  global legendarySword
  print("")
  if legendarySword == True:
    print("Your sword glows you then transform into the legendary hero that defeated the previous demon leader. Suddenly, you feel power and knowledge surging within you.\nYou feel as though you can take on the world if needed.")
    time.sleep(5)
    print("\nWhen you finish the fight you realize the sword has increased your base abilities strength,speed and mana. You see the dragon lying there.")
  else:
    print("You instead insist on using your own abilities to end the fight. You have become a better swordsman after your dungeon experience.")
    print("You best the dragon after battling with it for 30 minutes, the princess gives you a kiss on the cheek after saving her life not once but twice.")
  time.sleep(5)
  print("\nAt last you reach the home of the princess, where you receive the title of knight, the king's blessing. As well as money to live a fulfilling life.")
  print("                                 THE END")
  DragonDead = True
  gameOver()

def loseDragon():
  global legendarySword
  print("")
  if legendarySword == True:
    print("You try to hit the dragon with your the legendary sword, but its the hero's ability doesn't activate.")
    print("That was a mistake, the dragon releases its fire breath and disintegrates both you and the princess.")
  else:
    print("You swing your legendary sword and it hits, but the sword being too much to handle causes the dragon to get the upperhand.\nThe dragon then stands on you crushing your body with the weight of its foot.")
  gameOver()

def gameOver():
  print("")
  restart = input("Do you want to try again?").lower()
  if restart == "yes" or restart == "y" or restart == "ok":
    print("\n\n")
    start()
  elif restart == "no" or restart == "n":
    print("Goodbye... Quitter")
    quit()
  else:
    gameOver()

#program starts
legendarySword = True
DragonDead = False

name = input("What's your name?")
if name == "dragon":
  dragon()
start()

