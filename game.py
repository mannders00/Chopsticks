import os
import random

p1Left = 1
p1Right = 1

p2Left = 1
p2Right = 1

playing = True

def reset():
    global p1Left, p1Right, p2Left, p2Right

    p1Left = 1
    p1Right = 1
    p2Left = 1
    p2Right = 1

def check():
    global p1Left, p1Right, p2Left, p2Right, playing

    if p1Left > 4:
        p1Left = 0
    if p1Right > 4:
        p1Right = 0
    if p2Left > 4:
        p2Left = 0
    if p2Right > 4:
        p2Right = 0

    if p1Left == 0 and p1Right == 0:
        print("p2 wins!")
        playing = False
        return False
    elif p2Left == 0 and p2Right == 0:
        print("p1 wins!")
        playing = False
        return False

    return True

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

    usrInput = str(raw_input("Would you like to attack or split?: "))
    if usrInput == "attack":
        fromHand = str(raw_input("Would you like to attack from your left or right hand?: "))
        toHand = str(raw_input("Would you like to attack your opponent's left or right hand?: "))

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
        splitSide = str(raw_input("Would you like to transfer from the left or the right side?: "))
        splitAmount = input("How many would you like to transfer?: ")

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

def randomMove(type):
    #using random.randint(0, 2) == 0 as a series of coin-flip conditionals (other ways to do this)
    side = " "
    printName = " "
    enemyPrintName = " "
    if type == "player":
        side = "p1"
        printName = "Player 1"
        enemyPrintName = "Player 2"
    elif type == "enemy":
        side = "p2"
        printName = "Player 2"
        enemyPrintName = "Player 2"

    if random.randint(0, 2) == 0:
        #attack
        if random.randint(0, 2) == 0:
            #attack with left
            if random.randint(0, 2) == 0:
                #attack left with left
                attack(side + "Left", "left")
                return printName + " attacked " + enemyPrintName + "'s left hand with their left hand"
            else:
                #attack right with left
                attack(side + "Left", "right")
                return printName + " attacked " + enemyPrintName + "'s right hand with their left hand"
        else:
            #attack with right
            if random.randint(0, 2) == 0:
                #attack left with right
                attack(side + "Right", "left")
                return printName + " attacked " + enemyPrintName + "'s left hand with their right hand"
            else:
                #attack right with right
                attack(side + "Right", "right")
                return printName + " attacked " + enemyPrintName + "'s right hand with their right hand"
    else:
        #split
        if random.randint(0, 2) == 0:
            #split from left
            amount = random.randint(0, p2Left)
            split(side + "Left", amount)
            return printName + " split " + str(amount) + " from their left hand to their right hand"
        else:
            #split fron right
            amount = random.randint(0, p2Right)
            split(side + "Right", amount)
            return printName + " split " + str(amount) + " from their right hand to their left hand"

    return " "

def presetMove(side, moveID, quantity):
    #I define a split where quantity != -1
    #moveID for attack 0 = left to left, 1 = left to right, 2 = right to left, 3 = right to right
    #moveID for split 0 = left, 1 = right
    if quantity == -1:
        #attack
        if side == "p1":
            if moveID == 0:
                attack("p1Left", "left")
            elif moveID == 1:
                attack("p1Left", "right")
            elif moveID == 2:
                attack("p1Right", "left")
            elif moveID == 3:
                attack("p1Right", "right")
        elif side == "p2":
            if moveID == 0:
                attack("p2Left", "left")
            elif moveID == 1:
                attack("p2Left", "right")
            elif moveID == 2:
                attack("p2Right", "left")
            elif moveID == 3:
                attack("p2Right", "right")
    else:
        if side == "p1":
            if moveID == 0:
                split("p1Left", quantity)
            elif moveID == 1:
                split("p1Right", quantity)
        elif side == "p2":
            if moveID == 0:
                split("p2Left", quantity)
            elif moveID == 1:
                split("p2Right", quantity)

os.system("clear")
printStatus()

def tick():

    userMoveLog = userMove()
    check()
    os.system("clear")
    print("After P1 move: ")
    printStatus()

    if playing == True:
        enemyMoveLog = randomMove("enemy")
        check()
        print("After P2 move: ")
        printStatus()
        print(userMoveLog + "\n" + enemyMoveLog)

while playing:
    tick()
    check()
