def isPrime(x):
    if x == 1 or x == 0:
        return False

    for i in range(2,x-1):
        if x%i == 0:
            return False
    return True


#Driver code

print(isPrime(0))
