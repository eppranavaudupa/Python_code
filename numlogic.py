a=int(input("Enter the number : "))
        ##1)palindrome
def palindrome(a):
    num=0
    temp=a
    rev=0
    while temp>0:
        num=temp%10+num*10
        temp=temp//10
    # print(num)
        
    if(num==a):
        return(" yes it is a Palindrome")
    else:
        return("Not a Palindrome")
# print("checking palindrome : ",palindrome(a))

    #2)factorial
def factorial(a):
    fact=1
    for i in range(1,a+1):
        # print(i)
        fact = fact*i
    return fact
# print("Factorial of given number is : ",factorial(a))
        ##3)prime number
def prime_num(a):
    for i in range(2,a,1):
        # print(a%i)
            
        if(a%i==0):
            return False
        
    return True

        ##4)Prime Factors
def Prime_factor(a):
        
        for i in range(2,(a//2)+1):
            if(a%i==0 and prime_num(i)==True):

                print("prime factors :",i)
        if(prime_num(a)==True):
            print(a)
# print(Prime_factor(a))
        #5)Perfect square or not
def perfect_square(a):
    for i in range(1,a):
        if(a==i*i):
            print("Perfect squares are",i,"*",i)
            return
    print("Not a perfect square")
# perfect_square(a)

    ##6)Aramstrong number 153=1cube+5cube+3cube
def counter(a):
    count = 0
    num=0
    temp=a
    while temp>0:
        num=temp%10
        count+=1
        temp=temp//10
    return count
def aramstrong_num(a):
    count=counter(a)
    temp=a
    num=0
    total=0
    while temp>0:
        num=temp%10
        num=num**count
        total=total+num
        temp=temp//10
    if(total==a):
        return "Given number is Aramstrong number:",total
    return "Given number is not an Aramstrong number"
# print(aramstrong_num(a))
        #7)Strong number 
def strong_Number(a):
    temp=a
    total=0
    while temp>0:
        num=temp%10
        fact = factorial(num)
        total=fact+total
        temp=temp//10
    if(a==total):
        return("Given number is Strong number:",total)
    else:
        return("Not a Strong NUmber")
# print(strong_Number(a))
      #8)Perfect number ex:6=2+3+1 number which is equal to sum of its divisor
def perfect_num(a):
    temp=0
    total=0
    for i in range(1,a):
        if(a%i==0):
            num=i
            total=total+num
            if(total==a):
                return("The given number is a Perfect Number",total)
            
        else:
            return("Not a Perfect Number") 
        # return total
# print(perfect_num(a))  
        ##9)check whether a given number is a Harshad number or not.
def Harshad_num(a):
    temp=a
    num=0
    total=0
    while temp>0:
        num=temp%10
        total=total+num
        temp=temp//10
    if(a%total==0):
        return("Given number is Harshad Number:",a,"%",total,"= 0")
    else:
        return"not a Harshad Number"
# print(Harshad_num(a))
    #10) Write a program to check whether a given number is an Abundant number or not. 12=1+2+3+6 >16-->abundant
def abundant_num(a):
    temp=a
    total=0
    num=0
    for i in range(1,(a//2)+1):
        if(a%i==0):
            total=total+i
    if total > a :
        print("Abundant Number",total,">",a)
    else:
        print("Not Abundant Number")
# abundant_num(a)
        #11) Write a program to check whether a given number is an Automorphic number or not.5square=25 last digit(5) = number(5)
def Automorpic_num(a):
    num=counter(a)
    square=a*a
    print("square",square)
    extract=square%(10**num)
    print("extract",extract)
    if(extract==a):
        print("Number is Automorpic:",extract,"=",a)
    else:
        print("Not automorpic")
Automorpic_num(a)



