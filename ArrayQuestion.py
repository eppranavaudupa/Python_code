##1)Remove Duplicates
n=int(input("Enter No of Array Elements:"))
def User_input(n):
    arr=[]
    for i in range(n):
        U_input=int(input("Enter Elements:"))
        arr.append(U_input)
    return arr
def remove_ConsecutDuplicate(n):
    dup=[]
    arr=User_input(n)
    i=0
    j=1
    while j<=n-1:
        if(arr[i]!=arr[j]):
            dup.append(arr[i])
        j=j+1
        i=i+1
    dup.append(arr[i])
    print(dup)
# remove_ConsecutDuplicate(n)
def removeDup(n):
    arr=User_input(n)
    dup=[]
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i]!=arr[j] and arr[i] not in dup):
                dup.append(arr[i])
    dup.append(arr[i])
    return dup
# print(removeDup(n))
    #2)Find Missing Number
def missingNumBuilt(n):
    N=7
    arr=User_input(n)
    for i in range(n):
        if i not in arr:
            print(i)
# missingNumBuilt(n)
#N is the max element of your array
def missingNum(n):
    N=10
    sum=0
    arr=User_input(n)
    for i in range(n):
        sum+=arr[i]
    print(sum)
    print(int((N*(N+1))//2)-sum)
# missingNum(n)


