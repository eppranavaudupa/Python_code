n=5
def User_input(n):
    arr=[]
    for i in range(n):
        U_input=int(input("Enter Elements:"))
        arr.append(U_input)
    print(*arr)
# User_input(n)
def replacePositions(n):
    n=[3,3,3,3,3,3,3,3,3,3]
    for i in range(len(n)):
        if((i+1)%2==0):
            n[i]=0
        else:
            n[i]=1
    print(n)
# replacePositions(n)

n=int(input("Enter No of Array Elements:"))
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
# sumOfN(n)
def Max_MinEle(n):
    arr=[]
    for i in range(n):
        User_input=int(input("Enter Array Elements:"))
        arr.append(User_input)
    print(arr)
    max=0
    min=9
    for i in range(len(arr)):
        if(arr[i]>max):
            max=arr[i]
        if(arr[i]<min):
            min=arr[i]
    print("Max",max)
    print("Min",min)
# Max_MinEle(n)
def User_input(n):
    arr=[]
    for i in range(n):
        user_input=int (input("Enter Array Elements:"))
        arr.append(user_input)
    return arr
    #Search An Element in Array
def search_Ele(n):
    arr=User_input(n)
    search=int(input("The index you want to search : "))
    for i in range(search):
        if search==0:
            print(arr[0])
        if search>n:
            print("Not valid")
    else:
        print(arr[i])

# search_Ele(n)
def Odd_Even_Dig(n):
    evenArr=[]
    oddArr=[]
    while n: 
        num=n%10
        if(num%2==0):
            evenArr.append(num)
        else:
            oddArr.append(num)
        n=n//10
    print("Even Elements",evenArr)
    print("Odd Elements",oddArr)
# Odd_Even_Dig(n)
    #Reverse the Array
def ReverseArr(n):
    arr=User_input(n)
    i=0
    j=len(arr)-1
    while i<=j:
        t=arr[i]
        arr[i]=arr[j]
        arr[j]=t
        i+=1
        j-=1
    print(arr)
# ReverseArr(n)
    #[6,3,9,2,4,7]-->[2,4,7,6,3,9]
def half_rever(n):
    arr=User_input(n)
    i=0
    j=len(arr)-1
    while i<j:
        t=arr[i]
        arr[i]=arr[j]
        arr[j]=t
        i=i+1
        j=j-1
    print("arr",arr)
    arr2=arr
    k=len(arr)//2-1
    print("k",k)
    for i in range(len(arr)//2):
        temp=arr2[i]
        arr2[i]=arr2[k]
        arr2[k]=temp
        print("arr2",arr2)
# half_rever(n)
def reverseKth(n):
    arr=User_input(n)
    k=int(input("Number of Times array should Rotate"))
    for i in range(k):
        t=arr[(len(arr)-1)]
        for j in range((len(arr))-1,0,-1):
            arr[j]=arr[j-1]
        arr[0]=t
    print(arr)
# reverseKth(n)
def adder(n):
    arr=User_input(n)
    arr2=User_input(n)
    sortedarr1=sorted(arr)
    sortedarr2=sorted(arr2)
    total=sortedarr1+sortedarr2
    totalsorted=sorted(total)
    print(totalsorted)
adder(n)