def palindrome(strng):
    strng_without = strng.replace(" ","").lower()
    revstr =  strng_without[::-1]
    if revstr == strng_without :
        return True
    else:
        return False


def main():
   string = input('Enter a string : ')
   print(palindrome(string))


    


if __name__ == '__main__':
    main()


