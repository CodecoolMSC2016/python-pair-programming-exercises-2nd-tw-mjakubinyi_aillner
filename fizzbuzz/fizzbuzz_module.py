def fizzbuzz(number):
    if number%3 == 0 and number%5 == 0:
        return('FizzBuzz')
    elif number%3 == 0 :
        return('Fizz')
    elif number%5 == 0 :
        return('Buzz')
    elif number%3 != 0 and number%5 != 0:
        return(number)



def main():
    num_list = []
    for num in range(1,101):
        num_list.append(fizzbuzz(num))
        print(num_list[num-1])

print("__name__=" + __name__)
if __name__ == '__main__':
    main()
