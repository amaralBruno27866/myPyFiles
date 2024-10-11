class Solution2:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        def helper(nums, target, idx, hasher):
          if idx >= len(nums):
              return []
          current = nums[idx]
          if current in hasher:
              return [hasher[current], idx]
          hasher[target - current] = idx
          return helper(nums, target, idx + 1, hasher)
        
        return helper(nums, target, 0, {})

def test_two_sum_recursive():
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([1, 2, 3, 4, 5], 10, []),  # No solution case
    ]

    sol2 = Solution2()
    for nums, target, expected in test_cases:
        result = sol2.two_sum(nums, target)
        if result is None:
            result = []
        assert result == expected, f"Failed for {nums} with target {target}. Expected {expected}, got {result}"
    print("All tests passed for Solution2 class.")

if __name__ == "__main__":
    test_two_sum_recursive()