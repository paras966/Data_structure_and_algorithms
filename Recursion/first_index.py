'''Problem Statement: First Index
Problem Level: EASY
Problem Description:
Given an array of length N and an integer x, you need to find and return the first index of integer x present in the array. Return -1 if it is not present in the array.
First index means, the index of first occurrence of x in the input array.
Do this recursively. Indexing in the array starts from 0.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x

Output Format :
first index or -1

Constraints :
1 <= N <= 10^3

Sample Input :
4
9 8 10 8
8

Sample Output :
1'''
index=0
def firstIndex(arr,num):
    global index
    if len(arr)==0:
        return -1
    if (arr[0]==num):
        return index
    index+=1
    return firstIndex(arr[1:],num)

N=int(input())
elements = input().split(' ')
num = int(input("Enter number to be searched : "))
elements = [int(x) for x in elements]
print(firstIndex(elements, num))