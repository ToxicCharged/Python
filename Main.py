import TicTacToe
import numberGuesser
import Calculator
import Palindrome
import solidGeometry
import fibonacciNumber
import armstrongNumber
import reverseOfNumber
import Vowels

state = ""
while state.lower() != "n":

    print()
    print("1) Tic Tac Toe")
    print("2) Number Guesser")
    print("3) Calculator")
    print("4) Palindrome")
    print("5) Solid Geometry")
    print("6) Fibonacci Number")
    print("7) Armstrong Number")
    print("8) Reverse of Number")
    print("9) Vowels")
    print("x) Exit")
    print()
    choice = input("Choose an option: ")

    if choice == '1':
        TicTacToe.main()

    elif choice == '2':
        numberGuesser.main()

    elif choice == '3':
        Calculator.main()

    elif choice == '4':
        Palindrome.main()

    elif choice == '5':
        solidGeometry.main()

    elif choice == '6':
        fibonacciNumber.main()

    elif choice == '7':
        armstrongNumber.main()

    elif choice == '8':
        reverseOfNumber.main()

    elif choice == '9':
        Vowels.main()

    elif choice.lower() == 'x':
        print()
        print("Have a good day!")
        break

    else:
        print("Invalid choice.")
        continue

    print()
    state = str(input("Would you like to continue? (y/n) "))

    if state.lower() == 'n':
        print("Have a good day!")
    elif state.lower() != 'y':
        print("Invalid choice.")
