def main():

    print()
    num = int(input("Enter a number: "))
    temp = num
    sum = 0
    digits = len(str(num))

    temp = num

    while temp > 0:
        sum += (temp % 10) ** digits
        temp //= 10

    if sum == num:
        print("It is an armstrong number.")
    else:
        print("It is not an armstrong number.")


if __name__ == "__main__":
    main()
