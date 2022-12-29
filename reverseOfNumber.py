def main():

    print()
    num = int(input("Enter a number: "))
    temp = abs(num)
    rev_num = 0
    placeValue = len(str(num)) - 1

    while temp > 0:
        rev_num += (temp % 10) * 10 ** placeValue
        temp //= 10
        placeValue -= 1

    if num < 0:
        rev_num *= -1

    print("It's reverse =", rev_num)


if __name__ == "__main__":
    main()
