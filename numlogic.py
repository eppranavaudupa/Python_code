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
            # print("Perfect squares are",i,"*",i)
            return True
    # print("Not a perfect square")
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
        # return "Given number is Aramstrong number:",total
        return True
    # return "Given number is not an Aramstrong number"
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
        return True
        # return("Given number is Strong number:",total)
    # else:
        # return("Not a Strong NUmber")
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
                # return("The given number is a Perfect Number",total)
                return True
            
        # else:
            # return("Not a Perfect Number") 
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
        # return("Given number is Harshad Number:",a,"%",total,"= 0")
        return True
    # else:
        # return"not a Harshad Number"
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
        # print("Abundant Number",total,">",a)
        return True
    else:
        return False
        # print("Not Abundant Number")
# abundant_num(a)
        #11) Write a program to check whether a given number is an Automorphic number or not.5square=25 last digit(5) = number(5)
def Automorpic_num(a):
    num=counter(a)
    square=a*a
    # print("square",square)
    extract=square%(10**num)
    # print("extract",extract)
    if(extract==a):
        return True
        # print("Number is Automorpic:",extract,"=",a)
    else:
        return False
        # print("Not automorpic")
# Automorpic_num(a)
        ##12)Write a Program to check whether the number is Magic Number or Not
magicNumber=1 
def add(n):
        sum=0
        while n >0:
            sum +=n%10
            n=n//10
        return sum
def magic_Number(a):   
    b=add(a)
    # print(b)
    if(b>9 or b<9):
        res=add(b)
        if(res==magicNumber):
            return True
            # print(a,"It is a Magic Number")
        else:
            return False
            print("Not a Magic number") 
    # else:
    #     print("Not a Magic number")    
# magic_Number(a)
        #13)Write a program to check whether a given number is Friendly pair or not. (6,28) divisor of 6-->1+2+3+6=12    28-->1+2+4+7+14+28= 56 6/12=2 and 56/26=2 same 2 and 2 are getting
def Friendly_pair(a,b):
    sum1=0
    sum2=0
    for i in range(1,a+1):
        if(a%i==0):
            sum1+=i
    print("sum1",sum1)
    res1=sum1/a
    print("res1",res1)
    for j in range(1,b+1):
        if(b%j==0):
            sum2+=j
    print("sum2",sum2)
    res2=sum2/b
    print("res2",res2)
    if(res1==res2):
        print("friendly Pair")
    else:
        print("Not a Friendly pair")
# Friendly_pair(a,28)
        #14)Write a Program to check whether the number is Neon Number or Not. 9(square)=81 -->8+1=9 9 is Neon number
def Neon_num(a):
    num=0
    squre = a**2
    while squre>0:
        num+=squre%10
        squre//=10
    if(num==a):
        # print("Yes Its a Neon Number ",a,"=",num)
        return True
    else:
        return False
        print("Not a Neon Number")
# Neon(a)
        #15)Write a Program to check whether the number is Spy Number or Not 6=1+2+3=1*2*3
def Spy_num(a):
        
        sum=0
        mul=1
        for i in range(1,(a//2)+1):
            if(a%i==0):
                num=i
            # print("num",num)
            sum=sum+num
            mul=num*mul
            # print(sum,"sum")
            # print(mul,"mul")
        if(sum==mul):
            return True
            print("Spy Number",sum,"=",mul)
        else:  
            return False
            print("Not a Spy number")
# Spy_num(a)

        #16)Write a Program to check whether the number is Happy Number or Not.
def summer(a):
        temp=a
        sqr=0
        while temp>0:
            num=temp%10
            sqr+=num**2
            temp=temp//10
        return sqr   
def happy_Num(a):
    res=summer(a)
    # print("res ",res)
    while res>=10:
        res=summer(res)
        # print(res)

    # return ans
    if(res==1):
        # print("happy Number")
        return True
        
    else:
        return False
        print("NOT")
# happy_Num(a)
    #17)Write a Program to check whether the number is Sunny Number or Not. 8 is a sunny number 8+1=9 ,9 is a perfect square
def sunny_number(a):
        num=a+1
        for i in range(1,num):
            
            if(num == i*i):
                return True
                print("Sunny number",a)
        else:
            return False
            print("NOT")
# sunny_number(a)
        #18)Write a Program to check whether the number is Disarium Number or Not 89=8(to power 1)+9(to the power 2)=89
def Disarium(a):
    count=counter(a)
    temp=a
    power=0
    while temp>0:
        num=temp%10
        power=power+num**count
        # print("power",power)
        count=count-1
        temp=temp//10
    if(power==a):
        return True
        print("its a disarium number",power,"=",a)
    else:
        return False
        print("Not a disarium number")
# Disarium(a)
    #19)Write a Program to check whether the number is a Pronic Number or Not. product of two consecutive numbers
def pronic_number(a):
    for i in range(1,a):
        if(a%i==0):
            num=i*(i+1)
            if(num==a):
                return True
                print(" It is a Pronic number",num,"=",a)
                return
            else:
                return False
                print("Not a Pronic Number")
# pronic_number(a)
        #20)Write a Program to check whether the number is a Trimorphic Number or Not. A Trimorphic Number is a number whose cube ends in the same digits as the number itself.
def trimorpic(a):
    count=counter(a)
    num=a**3
    print("Cube of the Number",num)
    extract=num%10**count
    print("Extracted number",extract)
    if(extract==a):
        print("Its a Trimorpic number",a,"=",extract)
    else:
        print("not a trimorpic Number")
# trimorpic(a)
        #21)Program to check whether the number is an Evil Number or Not = number of 1's in its binary is even -->evil number
def Dec_to_bin(a):
    num=0
    n=1
    while a:
        num = a%2*n+num
        n=n*10
        a=a//2
    return num
Dec_to_bin(a)
def evil_num(a):
    num=Dec_to_bin(a)
    count=0
    while num:
        extract=num%10
        if(extract==1):
            count+=1
        num=num//10
    if(count%2==0):
        print("Given Number Is a Evil number","No of 1's","=",count)
    else:
        print("Not a Evil Number","No of 1's","=",count)
# evil_num(a)
        #22)program to find out all palindrome numbers present within a given range.
def reverse(i):
    rev=0
    num=0
    temp=i
    while temp:
        num=temp%10
        rev=num+rev*10
        temp=temp//10
    if(i==rev):
         True
    else:
        return False
def check_palindrome_range(a):
    for i in range(1,a+1):
        if(i<=10):
            b="All single Digit numbers are palindrome"
        elif(reverse(i)==True):
            print(i,"is a Palindrome")
    print(b)
# check_palindrome_range(a)
    #23)program to find out all primes numbers present within a given range
def prime_num_range(a):
        for i in range (2,a+1):
         if(prime_num(i)==True):
                print("Prime numbers are",i)
        
# prime_num_range(a)
        #24)program to find out all perfect square numbers present within a given range
def perfectSqr_range(a):
    for i in range(1,a+1):
        if(perfect_square(i)==True):
            print("perfect squares are:",i)
# perfectSqr_range(a)
    #25) program to find out all Armstrong numbers present within a given range
def ARAMSTRONG_RANGE(a):
    for i in range(1,a+1):
        if(aramstrong_num(i)==True):
            print("Aram stong Numbers:",i)
# ARAMSTRONG_RANGE(a)
    #26)program to find out all Strong numbers present within a given range
def STRONGNUM_RANGE(a):
    for i in range(1,a+1):
        if(strong_Number(i)==True):
            print("Strong Number:",i)
# STRONGNUM_RANGE(a)
    #27)program to find out all Perfect numbers present within a given range.
def PERFECTSQUARE_RANGE(a):
    for i in range(1,a):
        if(perfect_num(i)==True):
            print("Perfect NUmbers:",i)
# PERFECTSQUARE_RANGE(a)
    #28)program to find out all Harshad numbers present within a given range
def HARSHADNUMBERS_RANGE(a):
    for i in range(1,a):
        if(Harshad_num(i)==True):
            print("Harshad Numbers:",i)
# HARSHADNUMBERS_RANGE(a)
        #29)program to find out all Abundant numbers present within a given range
def ABUNDANTNUMBER_RANGE(a):
    for i in range(1,a):
        if(abundant_num(i)==True):
            print("abundant Number:",i)
# ABUNDANTNUMBER_RANGE(a)
    #30)program to find out all Automorphic numbers present within a given range.
def AUTOMORPIC_RANGE(a):
    for i in range(1,a):
        if(Automorpic_num(i)==True):
            print("Automorpic Numbers:",i)
# AUTOMORPIC_RANGE(a)
    #31)Program to Find out all Magic numbers present within a given range
def MAGICNUM_RANGE(a):
    for i in range(1,a):
        if(magic_Number(i)==True):
            print("Magic Number:",i)
# MAGICNUM_RANGE(a)
    #32)Program to Find out all Neon numbers present within a given range.
def NEONNUM_RANGE(a):
    for i in range(1,a):
        if(Neon_num(i)==True):
            print("Neon Numbers:",i)
# NEONNUM_RANGE(a)
    #33)Program to Find out all Spy numbers present within a given range.
def SPYNUM_RANGE(a):
    for i in range(1,a):
        if(Spy_num(i)==True):
            print("Spy numbers :",i)
# SPYNUM_RANGE(a)
        #34)a Program to Find out all Happy numbers present within a given
def HAPPYNUM_RANGE(a):
    for i in range(1,a):
        if(happy_Num(i)==True):
            print("happy numbers:",i)
# HAPPYNUM_RANGE(a)
        #35)Program to Find out all Sunny numbers present within a given range
def SUNNYnum_RANGE(a):
    for i in range(1,a):
        if(sunny_number(i)==True):
            print("sunny numbers:",i)
# SUNNYnum_RANGE(a)
    #36)Program to Find out all the Disarium numbers present within a given range.
def DISARIUMnum_RANGE(a):
    for i in range(1,a):
        if(Disarium(i)==True):
            print("Disarium numbers:",i)
# DISARIUMnum_RANGE(a)
    #37)Program to Find out all Pronic numbers present within a given range.
def PRONICnum_RANGE(a):
    for i in range(1,a):
        if(pronic_number(i)==True):
            print("Pronic NUmbers:",i)
PRONICnum_RANGE(a)          