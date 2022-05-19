'''Coding Problem
Problem Statement: Sum of array (recursive)
Problem Level: EASY
Problem Description:
Given an array of length N, you need to find and return the sum of all elements of the array.
Do this recursively.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces

Output Format :
Sum

Constraints :
1 <= N <= 10^3

Sample Input 1 :
3
9 8 9

Sample Output 1 :
26

Sample Input 2 :
3
4 2 1

Sample Output 2 :
7'''


def arraySum(arr):
    if len(arr)==0:
        return 0
    return arr[0]+arraySum(arr[1:])

N=int(input("Enter number of elements : "))
print("Enter list numbers :")
elements = input().split(' ')
elements = [int(x) for x in elements]
if len(elements)!=N:
    print("Please enter mentioned number of arguments !")
else:
    print(arraySum(elements))