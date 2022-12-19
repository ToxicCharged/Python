n = int(input("Enter the position of the fibonacci number: "))

fibonacciNumbers = [0, 1]
a = 0
b = 1
c = 0

for i in range(n):
    fibonacciNumbers.append(fibonacciNumbers[a] + fibonacciNumbers[b])
    a += 1
    b += 1

num = fibonacciNumbers[n]

if n == 1:
    print("The fibonacci number at the", str(n) + "st spot is:", num)
elif n == 2:
    print("The fibonacci number at the", str(n) + "nd spot is:", num)
else:
    print("The fibonacci number at the", str(n) + "th spot is:", num)
