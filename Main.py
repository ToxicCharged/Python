import Calculator
import Palindrome
import solidGeometry as geo

state = ""
while state.lower() != "n":
    print()
    print("1) Calculator")
    print("2) Palindrome")
    print("3) Solid Geometry")
    print("x) Exit")
    print()
    choice = input("Choose an option: ")

    if choice == '1':
        Calculator.main()

    elif choice == '2':
        Palindrome.main()

    elif choice == '3':
        geo.main()

    elif choice.lower() == 'x':
        print()
        print("Have a good day!")
        break

    else:
        print("Invalid choice.")
        continue

    print()
    state = str(input("Would you like to continue? (y/n) "))

    if state.lower() == "n":
        print("Have a good day!")
