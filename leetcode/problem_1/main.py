from typing import List
# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_c = 0
        cur_c = 0
        for n in nums:
            if n == 1:
                cur_c += 1
                if cur_c > max_c:
                    max_c = cur_c
            else:
                if cur_c > max_c:
                    max_c = cur_c
                    cur_c = 0
                else:
                    cur_c = 0
        return max_c