'''Problem Statement: Check Palindrome (recursive)
Problem Level: MEDIUM
Problem Description:
Check whether a given String S is a palindrome using recursion. Return true or false.
Input Format :
String S

Output Format :
'true' or 'false'

Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.

Sample Input 1 :
racecar

Sample Output 1:
true

Sample Input 2 :
ninja

Sample Output 2:
false'''

def palindrome(string):
    if(len(string)==0 or len(string)==1):
        return True
    if(string[0]==string[-1]):
        return palindrome(string[1:len(string)-1])
    else:
        return False

string=input()
print(palindrome(string))