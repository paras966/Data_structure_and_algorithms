'''Problem Statement: Last index of x
Problem Level: MEDIUM
Problem Description:
Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.
Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
You should start traversing your array from 0, not from (N - 1).
Do this recursively. Indexing in the array starts from 0.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x

Output Format :
last index or -1

Constraints :
1 <= N <= 10^3

Sample Input :
4
9 8 10 8
8

Sample Output :
3'''



a=-1
index=0
def lastIndex(arr,num):
    global index,a
    if len(arr)==0:
        if a>=0:
            return a
        else:
            return -1
    if arr[0]==num:
        a=index
    index+=1
    return lastIndex(arr[1:],num)


N=int(input())
elements = input().split(' ')
num = int(input("Enter number to be searched : "))
elements = [int(x) for x in elements]
print(lastIndex(elements, num))

