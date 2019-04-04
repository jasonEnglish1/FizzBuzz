def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


def main():
    start, end = input("Input the start and end values to test \n").split()
    for i in range(int(start), int(end)):
        fizz_buzz(i)


if __name__ == '__main__':
    main()
