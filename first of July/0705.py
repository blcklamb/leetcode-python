'''
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
'''

'테스트 코드에서 지속적으로 오류 발생 -> 조건부 처리를 잘 못함'

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        preprocessed = sorted(list(set(nums)))
        print(preprocessed)
        
        if len(preprocessed) == 0:
            return 0
        
        prevNum = min(preprocessed)
        maxLen = 1
        tempLen = 1
        
        for i in preprocessed[1:]:
            if prevNum + 1 == i:
                tempLen += 1
            else:
                if tempLen > maxLen:
                    maxLen = tempLen
                tempLen = 1
            prevNum = i
        if tempLen > maxLen:
            maxLen = tempLen
        return maxLen