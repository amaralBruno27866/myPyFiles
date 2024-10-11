class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hasher = {}
        for idx, i in enumerate(nums):
            if hasher.get(i) is not None:
                return [hasher.get(i), idx]
            hasher[target - i] = idx
        return []

def test_two_sum():
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([1, 2, 3, 4, 5], 10, []),  # No solution case
    ]

    sol = Solution()
    for nums, target, expected in test_cases:
        result = sol.twoSum(nums, target)
        assert result == expected, f"Failed for {nums} with target {target}. Expected {expected}, got {result}"
    print("All tests passed for Solution class.")

if __name__ == "__main__":
    test_two_sum()