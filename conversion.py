a = int(input("Enter the  numbers : "))
#decimal to bianry    
def dec(n):
    num=0
    pow=0
    while n:
        a=(n%10)*(2*pow)
        num=num+a
        pow+=1
        n//=10
    return num
#binary to oct
# print(dec(1111))
def oct(n):
    ans=0
    a=1
    while n >0:
        r=n%1000
        ans+=dec(r)*a
        a=a*10
        n//=1000
    return ans
# print(oct(763))
#decimal to binary
def dec_to_bin(n):
    ans = 0
    a = 1
    while n>0:
        ans = ans+(n%2)*a
        a = a*10
        n=n//2
    return (ans)
# print(dec_to_bin(a))
#octal to binary
def oct_to_bin(n):
    ans=0
    a=1
    while n>0:
        r=n%10
        s=dec_to_bin(r)
        ans=ans+s*a
        a=a*100
        n=n//a
    print(ans)
oct_to_bin(a)    
