'''You work in the message encoding department of a national security agency. Every message 
that is sent from or received in your office is encoded. You have an integer N, and each digit 
of N is squared and the squares are concatenated together to encode the original number. 
Your task is to find and return an integer value representing the encoded value of the 
number.
input1: An integer value N representing the number to be encoded.
Output :
Return an integer value representing the encoded value of the number.
Sample Input:
167
Sample Output:
13649'''
'''
msg=int(input("enter the message"))
list=[]
result=[]
for i in range:
     msg1=msg.spilt()
     list.append(msg1)
n=len(list)     
     
for i in range(0,n):
     res=list[i]*list[i]
     result.appent(res)
print(result)
     
'''

#------------------------------------------------------------------------------
'''Paul is given an array A of length N. He must perform the following Operations on the 
array sequentially:
* Choose any two integers from the array and calculate their average.
* If an element is less than the average, update it to 0. However, if the element is 
greater than or equal to the average, he need not update it.
Your task is to help Paul find and return an integer value, representing the minimum 
possible sum of all the elements in the array by performing the above operations.
Note: An exact average should be calculated, even if it results in a decimal.
Input Format:
input1: An integer value N, representing the size of the array A.
input2: An integer array A.
Output Format:
Return an integer value, representing the minimum possible sum of all the elements 
in the array by
Sample Input
5
1 2 3 4 5
Sample Output
5'''
def minsum(list,num):
    n=len(list)
    list.sort()
    max1,max2=list[-1],list[-2]
    avg=(max1+max2)/2
    sum=0
    for i in (n):
        if avg[i]<=avg:
            sum=sum+list[i]
        else:
            pass    
           

list1=list(map(int,input("enter the numbers").split()))
num=2
minsum(list1,num)
