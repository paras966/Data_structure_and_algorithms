'''Problem Statement: Count Zeros
Problem Level: EASY
Problem Description:
Given an integer N, count and return the number of zeros that are present in the given integer using recursion.
Input Format :
Integer N

Output Format :
Number of zeros in N

Constraints :
0 <= N <= 10^9

Sample Input 1 :
10204

Sample Output 1 :
2

Sample Input 2 :
708000

Sample Output 2 :
4'''
count = 0
def countZeros(num):
    global count
    if num==0:
        return 0
    local_variable = num%10
    if(local_variable==0):
        count+=1
    countZeros(num//10)
    return count

N=int(input())
print(countZeros(N))