def main():

    print()
    print("1) Number palindrome")
    print("2) Letter palindrome")
    print()
    choice = int(input("Choose an option: "))
    print()

    if choice == 1:

        num = int(input("Enter a number: "))
        numString = str(num)
        reverseNumString = numString[::-1]
        reverseNum = int(reverseNumString)

        if reverseNum == num:
            print("It is a palindrome.")
        else:
            print("It isn't a palindrome.")

    elif choice == 2:

        word = str(input("Enter a word: "))
        word = word.lower()
        reverseWord = word[::-1]

        if reverseWord == word:
            print("It is a palindrome.")
        else:
            print("It is not a palindrome.")

    else:
        print("Invalid choice.")
