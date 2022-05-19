'''Coding Problem
Problem Statement: Check number recursively
Problem Level: EASY
Problem Description:
Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
Do this recursively.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x

Output Format :
'true' or 'false'

Constraints :
1 <= N <= 10^3

Sample Input 1 :
3
9 8 10
8

Sample Output 1 :
true

Sample Input 2 :
3
9 8 10
2

Sample Output 2 :
false'''

def checkNumber(arr,num):
    if len(arr)==0:
        return False
    if (num==arr[0]):
        return True
    return checkNumber(arr[1:],num)

N=int(input("Enter number of array's elements : "))
num = int(input("Enter number to be searched : "))
print("Enter number (space seperated) ")

elements = input().split(' ')
elements = [int(x) for x in elements]
print(checkNumber(elements,num))