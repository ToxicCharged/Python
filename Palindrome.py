def main():

    print()
    print("1) Number palindrome")
    print("2) Letter palindrome")
    print()
    choice = int(input("Choose an option: "))
    print()

    if choice == 1:

        num = int(input("Enter a number: "))
        reverseNum = 0
        digits = -1

        if num > 0:
            temp = num
        else:
            temp = num * -1

        while temp > 0:
            temp //= 10
            digits += 1

        if num > 0:
            temp = num
        else:
            temp = num * -1

        while temp > 0:
            reverseNum += (temp % 10) * (10 ** digits)
            temp //= 10
            digits -= 1

        if reverseNum == abs(num):
            print("It is a palindrome.")
        else:
            print("It isn't a palindrome.")

    elif choice == 2:

        word = str(input("Enter a word: "))
        word = word.lower()
        tempWord = word
        reverseWord = ""

        for i in range(-1, -(len(word) + 1), -1):
            reverseWord += word[i]

        if reverseWord == word:
            print("It is a palindrome.")
        else:
            print("It isn't a palindrome.")

    else:
        print("Invalid choice.")
