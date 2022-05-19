'''Problem Statement: Sum of digits (recursive)
Problem Level: EASY
Problem Description:
Write a recursive function that returns the sum of the digits of a given integer.
Input format :
Integer N

Output format :
Sum of digits of N

Constraints :
0 <= N <= 10^9

Sample Input 1 :
12345

Sample Output 1 :
15

Sample Input 2 :
9

Sample Output 2 :
9'''

def digitSum(num):
    if(num==0):
        return 0
    return num%10 + digitSum(num//10)
n=int(input())
print(digitSum(n))
