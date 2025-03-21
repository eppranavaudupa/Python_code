n=9
def A(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or i==n//2 or j==n-1 or i==n-1 ):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
# A(n)
def b(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or i==n//2 or j==n-1 or i==n-1):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# b(n)
def c(n):
    for i in range(n):
        for j in range(n):
            if(j==0 or i==0 or i==n-1   ):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# c(n)
def e(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or i==n-1 or j==0 or i==n//2):
                print("*",end="")
            else:
                print("",end="")
        print()
# e(n)
def f(n):
    for i in range(n):
        for j in range(n):
            if  i==0 or j==0 or i==n//2:
                print("*",end="")
            else:
                print("",end=" ")
        print()
# f(n)
def g(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or i==n-1 or j==0 or j==n-1 and i>=n//2 or i==n//2 and j>=n//2) :
                print("*",end="")
            else:
                print(" ",end="")
        print()
# g(n)

def h(n):
    for i in range(n):
        for j in range(n):
            if(i==n//2 or j==0 or j==n-1):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# h(n)
def i (n):
    for i in range(n):
        for j in range(n):
            if(i==0 or i==n-1 or j==n//2):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# i(n)
def j(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==n-1 or i==n-1):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# j(n)
def k(n):
    for i in range(n):
        for j in range(n):
            if(j==0 or i+j==n-1 and i<=n//2 or i==n//2 and j<=n//2 or i-j==0 and i>=n//2):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# k(n)
def l(n):
    for i in range(n):
        for j in range(n):
            if(i==n-1 or j==0):
                print("*",end=" ")
            else:
                print(" ",end="")
        print()
# l(n)
def m(n):
    for i in range(n):
        for j in range(n):
            if(j==0 or j==n-1 or i-j==0 and i<=n//2 or i+j==n-1 and i<=n//2):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# m(n)
def N(n):
    for i in range(n):
        for j in range(n):
            if(i-j==0 or j==0 or j==n-1):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# N(n)
def o(n):
    for i in range(n):
        for j in range(n):
            if((j>=n//4 and i==0 and j<=3*n//4) or (i<=3*n//4 and j==0 and i>n//4) or (j<=3*n//4 and  i==n-1 and j>=n//4) or ( i<=3*n//4 and j==n-1 and i>n//4)or (j!=n-1 and i-j==0 and j!=0) or (j!=n-1 and i+j==n-1  and j!=0)):
                print("*",end="")
            else:
                print(" ",end="")
        print()
o(n)
def ComplexG(n):
    for i in range(n):
        for j in range(n):
            if( i==0 or j==0 or i==n-1 and j<=3*n//4 or j==n-1 and i>=n//4 or j==n-3 and i>=n//2 or j>=n//2 and i==n//2 and j<=3*n//4 or i<=3*n//4 and j==n//2 and i>=n//2 or i==3*n//4 and j<=n-6 and j>=n//4 or j==n//4 and i>=n//4 and i<3*n//4 or  i==n//4 and j>=n//4 and j<3*n//2 ):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# ComplexG(n)
def slantA(n):
    for i in range(n//2,n):
        for j in range(n):
            if((i-j==0 and i>n//2) or (i-j==0 and i+j==n-1)or (i+j==n-1 and i>n//2) or (i+j>=n-1 and i==3*n//4 and i-j>=0) ):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# slantA(n)

