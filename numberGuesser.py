import random


def main():
    print()
    print("I will guess the number you think of, with a little help from you.")
    print()
    print("Key:")
    print("h) Too high")
    print("l) Too low")
    print("c) Correct!!")
    print()

    a = int(input("Input minimum number: "))
    b = int(input("Input maximum number: "))
    tries = 0

    while True:

        tries += 1
        guess = random.randint(a, b)

        if tries == 1:
            feedback = str(input(f"Is {guess} right? "))
        elif tries == 2:
            feedback = str(input(f"What about {guess}? "))
        else:
            feedback = str(input(f"{guess}? "))

        if feedback.lower() == 'h':
            b = guess - 1

        elif feedback.lower() == 'l':
            a = guess + 1

        elif feedback.lower() == 'c':
            break

        else:
            print("Invalid.")

    print()
    print("ez")
    print(f"Number of tries: {tries}")


if __name__ == "__main__":
    main()
