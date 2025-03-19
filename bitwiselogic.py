    #making i th bit as 1
n=int(input("Enter the number"))
def logic1(n):
    num=n
    i=1
    print(num or 2**i)
# logic1(n)
# print(bin(11))
def josephus(n):
    power = 1
    while power * 2 <= n:
        power *= 2
    l = n - power
    return 2 * l + 1

# print("The safe position is:", josephus(n))
def CountZeros(n):
    count=0
    while n>0:
        if n%2==0:
            count+=1
            print(n)
        n=n//2
    print("count is",count)
# CountZeros(n)
def CountOne(n):
    count=0
    while n:
        if(n%2==1):
            count+=1
            # print(n)
        n=n>>1
    return(count)
# CountOne(n)
def countzeros2(n):
    count=0
    while n>0:
        if(n&1==0):
            count+=1
        n=n>>1
    return count
# print("COUNT NUM OF ZEROS (logic2)",countzeros2(n))
def powerof2(n):
    for i in range(n):
        if(n==2**i):
            print(n,"Can Be Represent as","2**",i)
# powerof2(n)
# a=8
def counter(a):
    count = 0
    num=0
    temp=a
    while temp>0:
        num=temp%10
        count+=1
        temp=temp//10
    return count
num=counter(n)
def powerof2_logic2(n):
    for i in range(1, n + 1):
        if CountOne(i) == 1:  
            print(i)
# powerof2_logic2(n)
def powerof2_logic3(n):
    num=0
    for i in range(2, n + 1):
        if (n&(n-1)==0):
            return True
        else:
            return False
    
# print(powerof2_logic3(n))
if((n-1)>>2==1):
    print (n)
else:
    print("No")