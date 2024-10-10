from typing import List
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    ones = 0
    twos = 0
    for i in nums:
      ones = (ones ^ i) & ~twos
      twos = (twos ^ i) & ~ones
    return ones
  
# Test
solution = Solution()
print(solution.singleNumber([2,2,2,3,1,1,1])) # 3