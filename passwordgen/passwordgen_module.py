import random
import string


def passwordgen():
    symbol = "!@#$%^&*()?"
    password_length = random.randint(4, 10)
    password = ""
    for i in range(0, password_length):
        character_type = random.randint(0, 2)
        if character_type == 0:
            password += string.ascii_letters[random.randint(0, 51)]
        elif character_type == 1:
            password += string.digits[random.randint(0, 9)]
        elif character_type == 2:
            password += symbol[random.randint(0, 10)]

    password += string.ascii_lowercase[random.randint(0, 25)]
    password += string.ascii_uppercase[random.randint(0, 25)]
    password += string.digits[random.randint(0, 9)]
    password += symbol[random.randint(0, 10)]

    return password


def main():
    print(passwordgen())


if __name__ == '__main__':
    main()
