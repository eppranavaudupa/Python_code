a=int(input("Enter the number : "))
        ##1)palindrome
def palindrome(a):
    num=0
    temp=a
    rev=0
    while temp>0:
        num=temp%10+num*10
        temp=temp//10
        
    if(num==a):
        return True
    else:
        return False
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
       
            if(a==i*(i+1)):
                # return True
                print(" It is a Pronic number")
                return
            else:
                # return False
                print("Not a Pronic Number")
# pronic_number(a)
        #20)Write a Program to check whether the number is a Trimorphic Number or Not. A Trimorphic Number is a number whose cube ends in the same digits as the number itself.
def trimorpic(a):
    count=counter(a)
    num=a**3
    # print("Cube of the Number",num)
    extract=num%10**count
    # print("Extracted number",extract)
    if(extract==a):
        return True
        print("Its a Trimorpic number",a,"=",extract)
    else:
        return False
        # print("not a trimorpic Number")
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
        return True
        print("Given Number Is a Evil number","No of 1's","=",count)
    else:
        return False
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
def pronic (a):
    for i in range(1,a):

        if((a==i*(i+1))):
            return True
            print("YES")
pronic(a)
def PRONICnum_RANGE(a):
    for i in range(1,a):
        if(pronic(i)==True):
            print("Pronic NUmbers:",i)
# PRONICnum_RANGE(a)     
        #38)Program to Find out all Trimorphic numbers present within a given range
def TRImorpic_RANGE(a):
    for i in range(1,a):
        if(trimorpic(i)==True):
            print("Trimorpic Numbers:",i)
# TRImorpic_RANGE(a)
    #39)Program to Find out all Evil numbers present within a given range.
def EVILnum_RANGE(a):
    for i in range(1,a):
        if(evil_num(i)==True):
            print("Evil numbers:",i)
# EVILnum_RANGE(a)
    #40)program to find the Generic root of a number. 456=4+5+6=15-->1+5=6 6 is the generic root of the number
def generic_root(a):
    temp=a
    sum=0
    ans=0
    num=0
    while temp:
        num=temp%10
        sum=num+sum
        temp=temp//10
    if( sum>9):
        ans=generic_root(sum)
    print("ANS",ans)
    return sum
# print(generic_root(a))
    #41)program to find out how many 1 and 0 in a given number.
def countbits(a):
    num=0
    count=0
    while a:
        num=num+a%2
        # print(num)
        count+=1
        a=a>>1
    print(count)
# countbits(a)
    #42)program to add between 2 numbers without using arithmetic operators.
def addition_withoutArithmaticOpr(a,b):
    while b>0:
        carry = a&b
        a = a^b
        b = carry<<1
    return a
# print(addition_withoutArithmaticOpr(15,3))
    #43)program to find the largest digit in a number
def largestDig(a):
    largest=0
    while a:
        num=a%10
        if(largest < num):
            largest=num
        a=a//10
    return largest
# print(largestDig(a))
    #44)program to find the smallest digit in a number.
def smallestDig(a):
    smallest=9
    while a:
        num=a%10
        if(smallest>num ):
            smallest=num
        a=a//10
    return smallest
# print(smallestDig(a))
        #45)a program to calculate Amicable pairs 220 and 284 -->divisors of sum of  220=284 and vice versa
def amicable_Pairs(a,b):
    sum=0
    sum2=0
    for i in range(1,a):
        if(a%i==0):
            sum=sum+i
    print("SUM",sum)
    print("b",b)
    for i in range(1,b):
        if(b%i==0):
            sum2+=i
    print("Sum2",sum2)
    print("a",a)
    if(sum == b and sum2 == a):
        print("Amicable Pairs")
        return
    else:
        print("Not ")
# amicable_Pairs(66928, 66992)  
    #46)a program to find the 2nd largest digit in a given number
def second_largest(a):
    first=0
    second=0
    while a>0:
        n=a%10
        if n>first:
            second=first
            first=n
        elif n>second and n<first:
            second=n
        a//=10
    return second
# print(second_largest(a))
    #47)program to find the 2nd smallest digit in a given number.
def second_Smallest(a):
    smallest=9
    secSmallest=0
    while a:
        n=a%10
        if n<smallest:
            secSmallest=smallest
            smallest=n
        elif n<secSmallest and n<smallest:
            secSmallest=n
        a=a//10
    print("Smallest",smallest)
    print("Second Smallest",secSmallest)
# second_Smallest(a)
    #48)Write a program to find the number of odd and even digits in the given number
def Odd_Even_Dig(a):
    evenArr=[]
    oddArr=[]
    while a: 
        num=a%10
        if(num%2==0):
            evenArr.append(num)
        else:
            oddArr.append(num)
        a=a//10
    print(evenArr)
    print(oddArr)
# Odd_Even_Dig(a)      
     #49)a program to check whether a given number is an ugly number.
def ugly_Num(a):
    for i in range(2,a):
        if(a%i==0 and prime_num(i)==True):
            num=i
            if(num==2 or num==3 or num==5):
                print("Ugly Num ")
        
# ugly_Num(a)
    #50)program to classify Abundant, deficient and perfect number (integers) between 1 to 10,000.
def classifyAB_DE_PER_NUM():
    abundant=[]
    perfect=[]
    deficient=[]
    for i in range(1,100):
        if(abundant_num(i)==True):
            abundant.append(i)
        if(abundant_num(i)==False):
            deficient.append(i)
        if(perfect_num(i)==True):
            perfect.append(i)
    print("Abundant Number",abundant)
    print("Perfect Number",perfect)
    print("deficient Number",deficient)
# classifyAB_DE_PER_NUM()
    #51)program to generate random integers in a specific range.
    #52)program to generate and show all Kaprekar numbers less than 1000.
def kaprekar_num(a):
    sqr=a**2
    temp=0
    temp=sqr
    sum=0
    while temp:
        num=temp%10
        print("num",num)
        sum=sum+num
        print("sum1",sum)
        if(sum!=a):
            num=temp%100
            sum=sum+num
            print("1st if",sum)
        if(sum!=a):
            num=temp%1000
            sum=sum+num
        temp=temp//10   
    if(sum==a):
        print(sum)
    else:
        print("NOT")
# kaprekar_num(a)
    #53)number of seed Lychrel number
def reverse(num):
    rev=0
    while num > 0:
        rev=num%10+rev*10
        num=num//10
    return rev
def lychrel_Num(a):
        
        temp=a
        for i in range(10):
            rev=reverse(temp)
            sum=temp+rev
            if(palindrome(sum)==True):
                return sum
            temp=sum
        return "Lynchrel Number"
print(lychrel_Num(a))


