n = int(input("Enter Number: "))
def prime_fact(a):
    for i in range(2,(a//2)):
        # print(i)
        if(a%i==0):
            return False
    return True
# print(prime_fact(n))
def factors(a):
    largest=0
    for i in range(1,a+1):
        if a%i==0 and prime_fact(i)==True:
            print(" Prime Factors:",i)
            if(largest<i):
                largest=i
        if(prime_fact(i)==n):
            largest=n
    print("largest",largest)
    # print("largest",largest)
factors(n)