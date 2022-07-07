'''
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
'''

class Solution:
    def fib(self, n: int) -> int:
        memo = [0, 1, 1]
        if n<=2:
            return memo[n]
        
        for i in range(3, n):
            memo.append(memo[i-2]+memo[i-1])
            
        return memo[n-2]+memo[n-1]