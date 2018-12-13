import os

p1Left = 1
p1Right = 1

p2Left = 0
p2Right = 0

#def reset():

def check():
    global p1Left, p1Right, p2Left, p2Right

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
        #reset()
    elif p2Left == 0 and p2Right == 0:
        print("p1 wins!")

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

#def transfer(side):

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

os.system("clear")
check()
printStatus()
