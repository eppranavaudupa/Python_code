n=15
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
triangleFilled(n)