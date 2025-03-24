n=5
def User_input(n):
    arr=[]
    for i in range(n):
        U_input=int(input("Enter Elements:"))
        arr.append(U_input)
    print(*arr)
# User_input(n)
def replacePositions(n):
    n=[1,2,3,4,5,6,7,8]
    for i in range(len(n)):
        if(n[i]%2==0):
            n[i]=0
        else:
            n[i]=1
    print(n)
# replacePositions(n)
n=int(input("Enter Array Elements:"))
def sumOfN(n):
    arr=[]
    for i in range(1,n+1):
        arr.append(i)
        print(arr[i-1],end="")
    sum=1
    for i in range(1,len(arr)):
        sum=sum*arr[i]
    print()
    print(sum)
sumOfN(n)
