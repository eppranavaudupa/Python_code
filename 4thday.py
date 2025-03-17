        #generating summation of each number and add those number 12345=summation(sum1+sum2+sum3+sum4+sum5)
a=int(input("ENTER THE NUMBER : "))
def summation_add(a):
    num=0
    sum=0
    total=0
    while a>0:
        num=a%10
        sum=((num*(num+1))/2)
        total=sum+total
        a=a//10
    return total
print("Summation of Each number is:",summation_add(a))


