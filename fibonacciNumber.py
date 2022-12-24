def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:

        return fibonacci(n - 1) + fibonacci(n - 2)


def main():

    print()
    num = int(input("Enter the position of the fibonacci number: "))

    if num == 1:
        print("The " + str(num) + "st fibonacci number is " + str(fibonacci(num)))
    elif num == 2:
        print("The " + str(num) + "nd fibonacci number is " + str(fibonacci(num)))
    elif num == 3:
        print("The " + str(num) + "rd fibonacci number is " + str(fibonacci(num)))
    else:
        print("The " + str(num) + "th fibonacci number is " + str(fibonacci(num)))
