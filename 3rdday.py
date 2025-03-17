    #1)power function using for loop
# def power(a, c):
#     result = 1
#     for _ in range(c):  
#         result =result* a  
#     return result

# a = 2
# c = 3
# print(power(a, c))  
    #2)power function using while loop
# def power(a,b):
#     res=1
#     while b>0:
#         res=res*a
#         b=b-1
#     return(res)

# 3)print(power(2,3))
    #counting number of digits
# number= int(input("Enter a number"))
# count=0
# while number>0:
#     number=number//10
#     count+=1
# print(count)
    #4)add two number without converting it into string
# a=1234
# b=77
# temp=b
# count=0
# while temp > 0:
#     temp=temp//10
#     count+=1
# print(count)
# a=a*(10**count)
# c=b+a
# print(c)
    # 5) remove the first digit of a number
# a=1234
# temp=a
# while temp > 10:
#     # digit=temp%10
#     temp=temp//10
# print(temp)
    #6) print numbers exept 1st number
# a=1234
# print("Given number is",a)
# temp = a
# count=0
# while temp>0:
#     temp=temp//10
#     count+=1
# for i in range(count):
#     a=a%(10**(count-1))
# print("result is",a)    
    #4)a=1234 b=77 o/p 1277
# a=1234
# b=77
# temp=b
# count=0
# while temp>0:
#     temp=temp//10
#     count+=1
# print(count)
# for i in range(count):
#     a=a//10
# print(a)
# a=a*(10**count)
# c=a+b
# print(c)
        #7)a=1234 b=77 o/p=771234
# a=1234
# b=77
# temp=a
# count=0
# while temp>0:
#     temp=temp//10
#     count+=1
# print(count)
# b=b*((10**count))
# c=b+a
# print("c is ",c)
        # 8)a=1234 b=77 o/p=7734
# a=int(input("ENTER 1ST NUMBER:"))

# b=int(input("ENTER 2nd number:"))

# temp=a
# count=0
# while temp>0:
#     temp=temp//10
#     count+=1
# print(count)
# b=b*(10**(count-2))
# a=a%(10**(count-2))
# print(a)
# c=b+a
# print(c)

        #9)length, reverse, maximum ,minimum, even_no ,odd_no, sum of digits, product of digits
a=231745
def lenght(a):
    count=0
    while a>0:
        a=a//10
        count+=1
    return count

# print(lenght(a))
def reverse(num):
    rev=0
    while num > 0:
        rev=num%10+rev*10
        num=num//10
    return rev

# print("Reversed number is : ",reverse(a))

def sum_num(a):
    temp=a
    sum=0
    while a > 0:
        sum = sum+a%10
        a=a//10
    return sum
    
# print("sum of the element is",sum_num(a))

def max_num(a):
    max=0
    num=0
    while a > 0:
        num=a%10
        if num > max:
            max=num
        a=a//10
    return max
# print("The maximum number is ",max_num(a))

def min_num(a):
    min=9
    while a > 0:
        num = a % 10
        if num < min:
            min=num
        a=a//10
    return min
# print("Minimum number  is :",min_num(a))

def even_no(a):
    while a>0:
        num=a%10
        if(num%2==0):
            # even=num
            print(num)
        a=a//10
    # return(even)    
#can be done in reverse logic also
# even_no(123485)

def mul_dig(a):
    num=1
    while a > 0 :
        num=a%10*num
        a=a//10
    return num

# print("multication of the dogit is:",mul_dig(1234))
    #encoding the number ex:12547 =01010
def encoder(a):
    enc=0
    place =1
    
    while a>0:
        num=a%10
        if num%2==0:
            num=1
        else:
            num=0
        enc=place*num+enc
        place*=10
        a=a//10
    return enc
# # print("Encoded number is:",encoder(12445544))
# a=hex(0x89%16)
# print(a)
# print(oct(0o45%8))
# print(bin(1100%2))
# print(64%10)
# print(51.45%7)
def length(n):
    b = 0
    a = 1    
    while n>0:
        c=n%10  
        if c%2==0:
            b += 1 * a  
        n //= 10  
        a *= 10  
    return b
# print(length(32581))
        #reversal of the two  number 
def grp_rev(a):
    rev=0
    num=0
    rev2=0
    while a>0:
        num=a%10
        print(num)
        rev=num%10+rev*10
        a=a//10
        # print("rev is ",rev)
    rev2=rev
    # print(rev2)
    dup=0
    while rev2>0:
        dup=rev2%100+dup*100
        rev2=rev2//100
        if(rev2<10 and rev2!=0):
            dup=dup*10+rev2
            print(dup)
            return
        print("length",lenght(rev2))
    print("FINAL",dup)    
grp_rev(123456)




