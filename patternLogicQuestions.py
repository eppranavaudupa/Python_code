n=9
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
# q4(n)
def q5(n):
    for i in range(n):
        for j in range(n):
            if(j>=n//2 and i<=n//2  or i>=n//2 and j<=n//2):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# q5(n)
def q6(n):
    for i in range(n):
        for j in range(n):
            if((i>=n//2 and i+j<=n-1 and j>=n//4 )):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# q6(n)
def q7(n):
    for i in range(n):
        for j in range(n//2,n):
            if( i+j>=n-1 and i-j<=0 or j>=n-1  ):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# q7(n)
def q8(n):
    for i in range(n//2,n):
        for j in range(n):
            if(not(i+j<=n-1 or i-j<0)) :
                print("*",end="")
            else:
                print(" ",end="")
# q8(n)
def q9(n):
    for i in range(n):
        for j in range(n):
            if((i+j<=n-1 and i-j>=0 )or i+j>=n-1 and i-j<=0 ) :
                print("*",end="")
            else:
                print(" ",end="")
        print()
# q9(n)
n=22    
for  i in range(0,n):
    for j in range(0,n):
        if (( j==0 and i>=n//2) or i==n-1 or (j==n-1 and i>=n//2) or
        ((i+j==n//2 or i-j==-n//2) or i==n//2)or
        ((j==n//4 and i>=3*n//4)or (i==3*n//4 and j>=n//4 and j<=n//2) or(j==n//2 and i>=3*n//4) )
        
        
        
        
        ):
            print("*",end="")
        else:
                print(" ",end="")
