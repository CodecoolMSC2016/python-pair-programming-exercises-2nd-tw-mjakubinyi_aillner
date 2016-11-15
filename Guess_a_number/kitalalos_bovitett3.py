import random

i = 1

running = True


def exit1():
    while True:
        new = input("Még egy játék? [\033[1mY/N\033[0m]:")
        if new == "Y" or new == "y":
            j = 1
            break
        elif new == "N" or new == "n":
            print("\n\033[1mKilépés\033[0m")
            running = False
        else:
            print("\n\033[1mÍrj Y vagy N karaktert!\033[0m \n")

while running:
    genRandNum = random.randrange(1, 101)
    print(
        "\n\033[1mGondoltam egy számra 1 és 100 között, 8 tipp-ből találd ki!\033[0m \n(X-re kilép!)\n")

    while i < 9:
        while True:
            userInput = input("{}. Tipp:".format(i))
            if userInput.isdigit():
                userInput = int(userInput)
                break
            elif userInput == "X" or userInput == "x":
                print("\n\033[1mKilépés\033[0m")
                exit()
            else:
                print("\033[1mSzámot írj be!\033[0m")

        if userInput == genRandNum:
            print("\033[1mTalált :)\033[0m \n")
            j = 0
            i = 1
            genRandNum = random.randrange(1, 101)
            exit1()
            if j == 1:
                break

        elif userInput < genRandNum:
            if (genRandNum - userInput) > 50:
                print(
                    "\033[1mTe kis csintalan, jóval nagyobbra gondoltam!!!\033[0m")
                i += 1
            else:
                print("\033[1mNagyobbra gondoltam!\033[0m")
                i += 1

        elif userInput > genRandNum:
            if (userInput - genRandNum) > 50:
                print(
                    "\033[1mTe kis butuska, jóval kisebbre gondoltam!!!\033[0m")
                i += 1
            else:
                print("\033[1mKisebbre gondoltam!\033[0m")
                i += 1

        if i == 9:
            print("\n\033[1mVesztettél :(\033[0m \n")
            j = 0
            i = 1
            genRandNum = random.randrange(1, 101)
            exit1()
            if j == 1:
                break
