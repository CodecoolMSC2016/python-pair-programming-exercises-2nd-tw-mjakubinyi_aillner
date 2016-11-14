import datetime


def years(age):
    date = datetime.datetime.now()
    turn_date = date.year + 100 - age
    return turn_date


def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(str(name) + "'s will turn 100 years old in : " + str(years(age)))

if __name__ == '__main__':
    main()
