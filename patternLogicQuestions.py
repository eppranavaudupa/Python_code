n=10
def triangleFilled(n):
    for i in range(n//2,n):
        for j in range(n):
            if(i==n-1 or (i-j==0 and  i>n//2) or (i+j==n-1 )):
                print(" ",end="")
            elif(i+j<=n-1 ):
                print(" ",end="")
            elif(i-j>=0):
                print("*",end="")
        print()
# triangleFilled(n)
def q1(n):
    for i in range(n):
        for j in range(n):
            if((i-j==0 and j<=n//2) or (i+j==n-1 and j<=n//2) or j==0):
                print(" ",end="")
            elif(i-j>0 and i+j<n-1 ):
                print("*",end="")
        print()
# q1(n)
def q2(n):
    for i in range(n):
        for j in range(n):
            if(((j<=n//2 and i<n//2)or i>=n//2 and j>=n//2) ):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# q2(n)
def q3(n):
    for i in range(n):
        for j in range(n):
            if(not(i>=n//2 and j>=n//4 and i+j<=n-1)):
                print("*",end="")
            else:
                print("$",end="")
        print()
# q3(n)
def q4(n):
    for i in range(n):
        for j in range(n):
            if(i+j>=n-1):
                print("*",end="")
            else:
                print(" ",end="")
        print()
q4(n)