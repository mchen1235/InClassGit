def divisors():
    number = int(input("Enter a number to get the positive divisors for: "))

    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

divisors()
