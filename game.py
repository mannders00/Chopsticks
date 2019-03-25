import os
import random
import tensorflow as tf
from tensorflow import keras
import numpy as np

p1Left = 1
p1Right = 1

p2Left = 1
p2Right = 1

playing = True

gameCount = 0
backlog = "" #  format = [p1Left, p1Right, p2Left, p2Right, move that is made]
             #  every time a move is made in a WINNING game, each move is recorded
             #  we assume that if a game is won, it's likely they made good moves
             #  this is the premise of the program. Each move is stored in backlog for every turn

#for starters, let's import our tensorflow model, which we'll use later
model = keras.models.load_model('chopsticks_model')

#now let's implement our game methods

def reset():
    global p1Left, p1Right, p2Left, p2Right

    p1Left = 1
    p1Right = 1
    p2Left = 1
    p2Right = 1

def check(decAndPrint=True):
    global p1Left, p1Right, p2Left, p2Right, playing, gameCount

    if p1Left > 4:
        p1Left = 0
    if p1Right > 4:
        p1Right = 0
    if p2Left > 4:
        p2Left = 0
    if p2Right > 4:
        p2Right = 0

    if p1Left == 0 and p1Right == 0:
        if decAndPrint:
            print("p2 wins!")
            gameCount = gameCount - 1
        playing = False
        return True
    elif p2Left == 0 and p2Right == 0:
        if decAndPrint:
            print("p1 wins!")
            gameCount = gameCount - 1
        playing = False
        return False

def attack(fromSide, toSide):
    global p1Left, p1Right, p2Left, p2Right

    if fromSide == "p1Left":
        if toSide == "right":
            p2Right = p2Right + p1Left
        elif toSide == "left":
            p2Left = p2Left + p1Left

    elif fromSide == "p1Right":
        if toSide == "right":
            p2Right = p2Right + p1Right
        elif toSide == "left":
            p2Left = p2Left + p1Right

    elif fromSide == "p2Left":
        if toSide == "right":
            p1Right = p1Right + p2Left
        elif toSide == "left":
            p1Left = p1Left + p2Left

    elif fromSide == "p2Right":
        if toSide == "right":
            p1Right = p1Right + p2Right
        elif toSide == "left"   :
            p1Left = p1Left + p2Right

def split(fromSide, amount):
    global p1Left, p1Right, p2Left, p2Right

    if fromSide == "p1Left":
        if p1Left >= amount and (p1Right + amount) <= 4:
            p1Left -= amount
            p1Right += amount
            return True
    elif fromSide == "p1Right":
        if p1Right >= amount and (p1Left + amount) <= 4:
            p1Right -= amount
            p1Left += amount
            return True
    elif fromSide == "p2Left":
        if p2Left >= amount and (p2Right + amount) <= 4:
            p2Left -= amount
            p2Right += amount
            return True
    elif fromSide == "p2Right":
        if p2Right >= amount and (p2Left + amount) <= 4:
            p2Right -= amount
            p2Left += amount
            return True
    else:
        return False

    return False

def printStatus():
    p2 = ""
    for i in range(0, 4 - p2Left):
        p2 = p2 + "-"
    for i in range(0, p2Left):
        p2 = p2 + "|"
    p2 = p2 + "   "
    for i in range(0, p2Right):
        p2 = p2 + "|"
    for i in range(0, 4 - p2Right):
        p2 = p2 + "-"

    print(p2)
    print("")

    p1 = ""
    for i in range(0, 4 - p1Left):
        p1 = p1 + "-"
    for i in range(0, p1Left):
        p1 = p1 + "|"
    p1 = p1 + "   "
    for i in range(0, p1Right):
        p1 = p1 + "|"
    for i in range(0, 4 - p1Right):
        p1 = p1 + "-"

    print(p1)

def userMove():

    usrInput = str(input("Would you like to attack or split?: "))
    if usrInput == "attack":
        fromHand = input("Would you like to attack from your left or right hand?: ")
        toHand = input("Would you like to attack your opponent's left or right hand?: ")

        if fromHand == "left":

            if toHand == "left":
                attack("p1Left", "left")
                return "Player 1 attacked Player 2's left hand with their left hand"
            elif toHand == "right":
                attack("p1Left", "right")
                return "Player 1 attacked Player 2's right hand with their left hand"
            else:
                print("Invalid input, try again")
                tick()

        elif fromHand == "right":

            if toHand == "left":
                attack("p1Right", "left")
                return "Player 1 attacked Player 2's left hand with their right hand"
            elif toHand == "right":
                attack("p1Right", "right")
                return "Player 1 attacked Player 2's right hand with their right hand"
            else:
                print("Invalid input, try again")
                tick()

        else:
            print("Invalid input, try again")
            tick()
    elif usrInput == "split":
        splitSide = str(input("Would you like to transfer from the left or the right side?: "))
        splitAmount = int(input("How many would you like to transfer?: "))

        if splitSide == "left":
            if split("p1Left", splitAmount) != True:
                print("Invalid input, try again")
                tick()
            else:
                return "Player 1 split " + str(splitAmount) + " from their left hand to their right hand"
        elif splitSide == "right":
            if split("p1Right", splitAmount) != True:
                print("Invalid input, try again")
                tick()
            else:
                return "Player 1 split " + str(splitAmount) + " from their right hand to their left hand"
        else:
            print("Invalid input, try again")
            tick()

    else:
        print("Invalid input, try again")
        tick()

    return " "


def presetMove(side, moveID):
    #Refer to reference for move ID
    # prefer not to use this many if statements, but since every condition uses the same
    # functions with different arguments, it's not easy to make an elegant solution in python

    if side == "p1":

        if moveID == 0:
            attack("p1Left", "left")
            return "Player 1 attacked Player 2's left hand with their left hand"
        elif moveID == 1:
            attack("p1Left", "right")
            return "Player 1 attacked Player 2's right hand with their left hand"
        elif moveID == 2:
            attack("p1Right", "left")
            return "Player 1 attacked Player 2's left hand with their right hand"
        elif moveID == 3:
            attack("p1Right", "right")
            return "Player 1 attacked Player 2's right hand with their right hand"
        elif moveID == 4:
            split("p1Left", 1)
            return "Player 1 split 1 from their left hand to their right hand"
        elif moveID == 5:
            split("p1Left", 2)
            return "Player 1 split 2 from their left hand to their right hand"
        elif moveID == 6:
            split("p1Left", 3)
            return "Player 1 split 3 from their left hand to their right hand"
        elif moveID == 7:
            split("p1Left", 4)
            return "Player 1 split 4 from their left hand to their right hand"
        elif moveID == 8:
            split("p1Right", 1)
            return "Player 1 split 1 from their right hand to their left hand"
        elif moveID == 9:
            split("p1Right", 2)
            return "Player 1 split 2 from their right hand to their left hand"
        elif moveID == 10:
            split("p1Right", 3)
            return "Player 1 split 3 from their right hand to their left hand"
        elif moveID == 11:
            split("p1Right", 4)
            return "Player 1 split 4 from their right hand to their left hand"

    elif side == "p2":

        if moveID == 0:
            attack("p2Left", "left")
            return "Player 2 attacked Player 1's left hand with their left hand"
        elif moveID == 1:
            attack("p2Left", "right")
            return "Player 2 attacked Player 1's right hand with their left hand"
        elif moveID == 2:
            attack("p2Right", "left")
            return "Player 2 attacked Player 1's left hand with their right hand"
        elif moveID == 3:
            attack("p2Right", "right")
            return "Player 2 attacked Player 1's right hand with their right hand"
        elif moveID == 4:
            split("p2Left", 1)
            return "Player 2 split 1 from their left hand to their right hand"
        elif moveID == 5:
            split("p2Left", 2)
            return "Player 2 split 2 from their left hand to their right hand"
        elif moveID == 6:
            split("p2Left", 3)
            return "Player 2 split 3 from their left hand to their right hand"
        elif moveID == 7:
            split("p2Left", 4)
            return "Player 2 split 4 from their left hand to their right hand"
        elif moveID == 8:
            split("p2Right", 1)
            return "Player 2 split 1 from their right hand to their left hand"
        elif moveID == 9:
            split("p2Right", 2)
            return "Player 2 split 2 from their right hand to their left hand"
        elif moveID == 10:
            split("p2Right", 3)
            return "Player 2 split 3 from their right hand to their left hand"
        elif moveID == 11:
            split("p2Right", 4)
            return "Player 2 split 4 from their right hand to their left hand"

os.system("clear")

while True:
    gameOption = input("Do you want to play against the computer or run the simulation? (play / sim): ")
    if gameOption == "play" or gameOption == "sim":
        if gameOption == "sim":
            while True:
                gameCount = input("How many simulations would you like to do?: ")
                if gameCount.isdigit():
                    gameCount = int(gameCount)
                    break
                else:
                    print("Invalid input, try again")
        break
    else:
        print("Invalid input, try again")

printStatus()

def tick():
    global backlog, gameCount, playing

    if gameOption == "play":
        userMoveLog = userMove()    
        os.system("clear")
    else:
        userMoveLog = presetMove("p1", random.randint(0,12))
    check()
    if gameOption == "play":
        print("After P1 move: ")
        printStatus()

    if playing == True:
        enemyMove = None
        if gameOption == "play":
            prediction = model.predict(np.array([[p1Left,p1Right,p2Left,p2Right]]))
            enemyMove = np.argmax(prediction[0])
        else:
            enemyMove = random.randint(0, 12)
        enemyMoveLog = presetMove("p2", enemyMove)
        check()
        if gameOption == "play":
            print("After P2 move: ")
            printStatus()
            if userMoveLog is not None and enemyMoveLog is not None:
                print(userMoveLog + "\n" + enemyMoveLog)

        #add current game move state to the log
        backlog = backlog + str(p1Left) + " " + str(p1Right) + " " + str(p2Left) + " " + str(p2Right) + " " + str(enemyMove) + "\n"
        #format = [p1Left, p1Right, p2Left, p2Right, move that is made]

        if check(False): #if p2 wins, we add our backlog to the text file
            with open("output.txt", 'a') as f:
                f.write(backlog + "\n")

    if playing == False and gameCount > 0:
        playing = True
        print("Resetting game...")
        backlog = ""
        reset()

while playing:
    tick()
    check()