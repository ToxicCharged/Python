import Calculator
import Palindrome
import solidGeometry
import armstrongNumber
import reverseOfNumber
import Vowels

state = ""
while state.lower() != "n":
    print()
    print("1) Calculator")
    print("2) Palindrome")
    print("3) Solid Geometry")
    print("4) Armstrong Number")
    print("5) Reverse of Number")
    print("6) Vowels")
    print("x) Exit")
    print()
    choice = input("Choose an option: ")

    if choice == '1':
        Calculator.main()

    elif choice == '2':
        Palindrome.main()

    elif choice == '3':
        solidGeometry.main()

    elif choice == '4':
        armstrongNumber.main()

    elif choice == '5':
        reverseOfNumber.main()

    elif choice == '6':
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
