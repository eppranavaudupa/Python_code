n = int(input("Enter Number: "))

def prime(a):
    if a < 2:
        return False
    for j in range(2, int(a ** 0.5) + 1):  # Check up to sqrt(a)
        if a % j == 0:
            return False
    return True  # Only return True after checking all numbers

def checker(n):
    print("Prime factors:")
    for i in range(2, n + 1):
        if n % i == 0 and prime(i):  # Check if i is a factor and prime
            print(i)

checker(n)  # Call checker to find prime factors
