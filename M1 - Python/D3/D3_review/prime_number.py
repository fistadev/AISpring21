y = int(input())


def is_prime(n):
    i = 2
    while i < n-1:
        if round(n / i) == n / i:
            prime = False
            break
        i += 1
    else:
        prime = True
    if n == 1:
        prime = False
    print(prime)


is_prime(y)


# explanation
def is_prime(x):
    # primes divide by 1 and themsleves as do all numbers so we don't need to check that
    # run a for loop the checks if the number divides everything from 2 up to 1 less then the input
    for y in range(2, x):
        r = x % y
        # if reminder is 0 then must divdie and the number is not prime so return false
        if r == 0:
            return False
    # if is gets all the way through without returning false it must be a prime number so return true
    return True


is_prime(15)


# def is_prime(number):
#     counter = []

#     for i in range(1, number + 1):
#         counter.append(number % i)
#     return counter.count(0) <= 2

# def all_primes(maximum):
#     for i in range(2, maximum + 1):
#         if is_prime(i):
#             print(i, end = " ")

# all_primes(20)
