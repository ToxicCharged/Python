def main():

    print()
    print("This is a calculator.")
    print()

    print("Your options are:")
    print("+ -> Add")
    print("- -> Subtract")
    print("* -> Multiply")
    print("/ -> Divide")
    print("^ -> Exponent")
    print()

    x = float(input("Enter number: "))
    print()
    answer = x

    while True:
        operator = str(input("Enter operator: "))
        print()

        if operator == '=':
            break
        elif not (operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '^'):
            print("Invalid operator.")
            print()
            continue

        y = float(input("Enter number: "))
        print()

        if operator == '+':
            answer += y
        elif operator == '-':
            answer -= y
        elif operator == '*':
            answer *= y
        elif operator == '/':
            answer /= y
        elif operator == '^':
            answer **= y
        else:
            print("Invalid operator.")

    print("Answer: " + str(answer))
    print()
