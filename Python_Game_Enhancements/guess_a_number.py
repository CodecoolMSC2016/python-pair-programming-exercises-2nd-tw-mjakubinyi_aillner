import random
import datetime
import os
from window import *


def tipp_input(tipp_counter):
    valid_input = False
    while not valid_input:
        user_input = input("{}. Tipp:".format(tipp_counter))
        try:
            user_input = int(user_input)
            valid_input = True
        except(ValueError):
            print("\033[1m" + "Számot írj be!" + "\033[0m")
        if user_input == "X" or user_input == "x":
            print("\n" + "\033[1m" + "Kilépés" + "\033[0m")
            exit()

    return user_input


def message(size, chooser):
    # random generál becézéseket
    names = ["csintalan", "butuska", "gógyi"]
    if chooser == "short":
        text = ("{} gondoltam!".format(size))
    else:
        text = ("{} gondoltam jóval, te kis {}!!!".format(
            size, random.choice(names)))
    # itt hívja meg a külső file-ból importált függvényeket
    create_window()
    write_message(text)


def write_to_file(user_name, tipp_counter, win):
    date = datetime.datetime.now()
    my_file = open("result.txt", "a+")
    # beírja a file-ba, a nevet, a tippek számát, nyert-e, és a nyerés idejét
    my_file.write(user_name + "," + str(tipp_counter) + "," + str(win) + "," +
                  str(date) + "\n")
    my_file.close()


def exit_game():
    while True:
        new = input("Még egy játék?" +
                    "\033[1m" + " [Y/N]" + "\033[0m" + ":")
        if new == "Y" or new == "y":
            os.system("clear")
            print("\033[33m" + "Új játék!" + "\033[0m" + "\n")
            break
        elif new == "N" or new == "n":
            print("\n\033[1m" + "Kilépés" + "\033[0m")
            exit()
        else:
            print("\n\033[1m" + "Írj Y vagy N karaktert!" + "\033[0m" + "\n")


def main():
    os.system("clear")
    tipp_counter = 1
    max_tipp = 8
    running = True
    user_name = input("Add meg a neved:")

    while running:
        gen_rand_num = random.randrange(1, 101)
        print(
            "\n\033[1m" + "Gondoltam egy számra 1 és 100 között, 8 tipp-ből találd ki!" + "\033[0m" + " \n(X-re kilép!)\n")
        print(gen_rand_num)  # a gyorsabb teszteléshez

        while tipp_counter <= max_tipp:
            user_input = tipp_input(tipp_counter)

            if user_input == gen_rand_num:
                print("\n" + "\033[92m" + "Talált :)" + "\033[0m" + "\n")
                tipp_counter = 1
                max_tipp -= 1
                print("Következő szint! Már csak {} találatod van! \n".format(max_tipp))
                # újabb random szám generálása, a nehezebb szinthez
                gen_rand_num = random.randrange(1, 101)
                print(gen_rand_num)  # a gyorsabb teszteléshez
                if max_tipp < 3:
                    print(
                        "\n" + "\033[92m" + "Megynyerted a játékot :) :) :)" + "\033[0m" + "\n")
                    # eredmények txt-be írása
                    win = True
                    write_to_file(user_name, tipp_counter, win)
                    tipp_counter = 1
                    max_tipp = 8
                    exit_game()

            elif user_input > 100 or user_input < 1:
                print("\033[1m" + "1 és 100 közöttit írj be!!!" + "\033[0m")

            elif user_input < gen_rand_num:
                size = "Nagyobbra"
                if (gen_rand_num - user_input) > 50:
                    message(size, "long")
                    tipp_counter += 1
                else:
                    message(size, "short")
                    tipp_counter += 1

            elif user_input > gen_rand_num:
                size = "Kisebbre"
                if (user_input - gen_rand_num) > 50:
                    message(size, "long")
                    tipp_counter += 1
                else:
                    message(size, "short")
                    tipp_counter += 1

            if tipp_counter > max_tipp:
                print("\n\033[93m" + "Vesztettél :(" + "\033[0m" + "\n")
                # eredmények txt-be írása
                win = False
                write_to_file(user_name, tipp_counter - 1, win)
                # újabb random szám generálása, ha új játék kezdődne
                tipp_counter = 1
                gen_rand_num = random.randrange(1, 101)
                exit_game()


if __name__ == "__main__":
    main()
