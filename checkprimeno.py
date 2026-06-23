def isPrime(x):
    if x <= 1:
        return False

    for n in range(2, x):
        if x % n == 0:
            return False

    return True


array = [44, 76, 24, 86, 89]

for num in array:
    if isPrime(num):
        print(num, ": yes prime number")
    else:
        print(num, ": no prime number")