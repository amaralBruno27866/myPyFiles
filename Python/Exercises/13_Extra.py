from typing import List
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    ones = 0
    twos = 0
    for i in nums:
      ones = (ones ^ i) & ~twos
      twos = (twos ^ i) & ~ones
    return ones

"""
Analysis

#1 Set variables

-------------------------------------------------------------------------------

#2 Count operations

-------------------------------------------------------------------------------

#3 Mathematical expression

-------------------------------------------------------------------------------

#4 Simplify expression

-------------------------------------------------------------------------------

#5 Final result (complexity)

-------------------------------------------------------------------------------

"""

solution = Solution()
print(solution.singleNumber([2,2,2,3,1,1,1])) # 3