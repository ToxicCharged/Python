def main():

    print()
    string = input("Enter a string: ")
    vowels = 0
    print("The vowels are:", end=" ")

    for ch in string:

        if ch.lower() == 'a' or ch.lower() == 'e' or ch.lower() == 'i' or ch.lower() == 'o' or ch.lower() == 'u':
            print(ch, end=" ")
            vowels += 1

    print()
    print("Number of vowels :", vowels)


if __name__ == "__main__":
    main()
