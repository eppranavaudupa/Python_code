a = str(input("Enter the  numbers : "))
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
# oct_to_bin(a)    
## binary to Hexadecimal
def bin_to_dec(n):
    num=0
    pow=0
    while n:
        a=(n%10)*(2**pow)
        num=num+a
        pow+=1
        n//=10
    return num
# print(bin_to_dec(a))    

def bin_to_Hexa(a):
    temp=a
    val=0
    str=""
    while temp > 0 :
        num=temp%10000
        val=bin_to_dec(num)
        # print(val)
        if val>=10:
            asci=val+55
            ans=chr(asci)
        else:
            ans=chr(val+48)
            # print(ans)
            
        str=ans+str
        temp=temp//10000
    return("string",str)
    # print("CHR",ans)
    # str=str+ans
    # print("string",str)

    # return val
# print(bin_to_Hexa(a))
    ##converting Hexadeciaml to binary
def Hexa_to_bin(a):
    res=0
    ans=0
    for i in range(len(a)):
        asci=ord(a[i])
        value=asci-55
        res=dec_to_bin(value)
        ans=res+ans *10000
    print("RES",ans)
Hexa_to_bin(a)
