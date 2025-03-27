n=int(input("Enter No of Array Elements:"))
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
def ReverseArr(arr):
    i=0
    j=len(arr)-1
    while i<=j:
        t=arr[i]
        arr[i]=arr[j]
        arr[j]=t
        i+=1
        j-=1
    return arr
# ReverseArr(n)
    #[6,3,9,2,4,7]-->[2,4,7,6,3,9]
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
def adderUsingSortFn(n):
    arr=User_input(n)
    arr2=User_input(n)
    sortedarr1=sorted(arr)
    sortedarr2=sorted(arr2)
    total=sortedarr1+sortedarr2
    totalsorted=sorted(total)
    print(totalsorted)
# adderUsingSortFn(n)
    #second Largest element and Third Largest Element in an list
def sec_ThirdLarge(n):
    arr=User_input(n)
    max=0
    secLar=0
    thirdLar=0
    for i in range(len(arr) ):
        if(arr[i]>max):
            thirdLar=secLar
            secLar=max
            max=arr[i]
        elif(secLar<arr[i] and arr[i]<max):
            thirdLar=secLar
            secLar=arr[i]
        elif(thirdLar<arr[i] and arr[i]<secLar):
            thirdLar=arr[i]
    print(thirdLar,"thirdLar")
    print (secLar)
# sec_ThirdLarge(n)
    #swaping-->3,7,9,2,5,4==>7,3,2,9,4,5
def swaping(n):

    arr=User_input(n)
    i=0
    j=1
    temp=0
    while i<n-1:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i=i+2
        j=j+2
    print(arr)
# swaping(n)
def swaping2(n):
    arr=User_input(n)
    for i in range(0,n-1,2):
        t=arr[i]
        arr[i]=arr[i+1]
        arr[i+1]=t
    print(arr)
# swaping2(n)
    #Even index First
def evenind_Fir(n):
    arr=User_input(n)
    b=[]
    j=0
    for i in range(0,n,2):
        b.append(arr[i])
        j+=1
    for i in range(1,n,2):
        b.append(arr[i])
        j+=1
    print(b)
# evenind_Fir(n)
    ##maximum product of triplet in an array
def max_prod_Trip(n):
    arr=User_input(n)
    max=0
    secmax=0
    thirdmax=0
    for i in range(len(arr)):
        if(max<arr[i]):
            thirdmax=secmax
            secmax=max
            max=arr[i]
        elif(secmax<arr[i] and arr[i]<max):
            thirdmax=secmax
            secmax=arr[i]
        elif(thirdmax < arr[i] and arr[i] < secmax):
            thirdmax=arr[i]
            print(thirdmax)
    product=[max*secmax*thirdmax]
    print(product)
# max_prod_Trip(n)
def lesserNumberFirst1(n):
    x=7
    b=[]
    arr=User_input(n)
    for i in range(n):
        if(arr[i]<x):
            b.append(arr[i])
    for j in range(n):
        if(arr[j]==x):
            b.append(arr[j])
        if(arr[j]>x):
            b.append(arr[j])
    print(b)
# lesserNumberFirst1(n)
def linearSearch(n):
    k=5
    arr=User_input(n)
    for i in range(n-1,-1,-1):
        if(arr[i]==k):
            print(i)
# linearSearch1(n)
def linearSearch(n):
    k=5
    arr=User_input(n)
    for i in range(n):
        if(arr[i]==k):
            print(i)
# linearSearch1(n)
    #Maximum consecutive one’s (or zeros) in a binary array
def maxCount_0_1(n):
    arr=User_input(n)
    count=0
    j=0
    for i in range(1,len(arr)):
        print(i)
        if(arr[i]==arr[j]):
            count+=1
            j+=1
        else:
            j+=1

    print("count",count)
# maxCount_0_1(n)
        #Prefix sum
# def prefix_sum(n):
def left_sum():
    arr=[10,4,8,3]
    ls=[0]
    rs=[0]
    prefixSum=[]
    sum=0
    rsum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
        ls.append(sum)
    print(ls)
    for i in range(len(arr)-1,-1,-1):
        rsum=rsum+arr[i]
        rs.append(rsum)
    rghtSum=ReverseArr(rs)
    print(rghtSum)
    for i in range(len(ls)):
        prefixSum.append(abs(rghtSum[i]-ls[i]))
        # return prefixSum
    # prefixSum = [abs(rghtSum[i] - ls[i]) for i in range(len(ls))]
    print(prefixSum,'prefixSum')
# left_sum()
        ##Binary Search
def binarySearch(n):
    arr=User_input(n)
    key=6
    low=0
    high=len(arr)
    mid=(low+high)//2
    while low>=high:
        if(arr[mid]==key):
            return mid
        elif(arr[mid]>key):
            high=mid-1
        elif(arr[mid]<key):
            low=mid+1
    print(mid)
# print(binarySearch(n))
def countConcecuteOne(n):
    arr=User_input(n)
    count=0
    fc=0
    for i in range(len(arr)):
        if(arr[i]==1):
            count+=1
        else:
            if(count>fc):
                fc=count
            count=0
            if(count<fc):
                fc=count
    print(fc)
# countConcecuteOne(n)
def a(n):
    arr=User_input(n)
    count=0
    maxCount=0
    for i in range(n):
        if(arr[i]==1):
            count=count+1
        
        else:
            maxCount=max(count,maxCount)
            count=0
    maxCount=max(count,maxCount)
    return maxCount
# print(a(n))
        #1)
class Solution:
    def maxConsecutiveCount(self, arr):
        #code here 
        count=1
        maxCount=0
        for i in range(1,len(arr)):
            if(arr[i]==arr[i-1]):
                count+=1
            else:
                maxCount=max(maxCount,count)
                count=1
        maxCount=max(maxCount,count)
        return maxCount
    ##pushing 0's at last
def pushing0(n):
    arr=User_input(n)
    j=len(arr)-1
    i=0
    while i<=j:
        if(arr[i]==0):
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
        j=j-1
        i+=1
    print(arr) 
# pushing0(n)
def pushingZero_Last(n):
    arr=User_input(n)
    j=0
    i=0
    while arr[j]!=0:
        j+=0
        print("1j",arr[j])
        for i in range(j+1,len(arr)):
            if(arr[i]!=0):
                print("2j",arr[j],arr[i])
                arr[j]=arr[i]
                j+=1
                print("+3",arr[j])
        for i in range(j,len(arr)):
            print("2nd For",arr[i])
            arr[i]=0
            print("2nd For 2nd element",i)
    return arr
# print(pushingZero_Last(n))
    ##reverse Array in group
def revArr_Grp(n):
    arr=User_input(n)
    k=int(input("Number Elements to rotate:"))
    i=0
    j=k-1
    if(k>=n or k==1):
        ReverseArr(arr)
        return arr
    else:
        while j<=n-1:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j+=k
            i+=k
        return arr
# print(revArr_Grp(n))
        ##Selection Sorting
def selection_Sort(n):
    arr=User_input(n)
    for i in range(0,len(arr),1):
        for j in range(i+1,len(arr),1):
            if(arr[i]>arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
    return arr
print(selection_Sort(n))
            
