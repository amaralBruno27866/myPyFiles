class Solution2:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        def helper(nums, target, idx, hasher):
            print(f"helper called with idx={idx}, hasher={hasher}")
            if idx >= len(nums):
                print("Reached end of list, returning []")
                return []
            current = nums[idx]
            if current in hasher:
                print(f"Found solution: [{hasher[current]}, {idx}]")
                return [hasher[current], idx]
            hasher[target - current] = idx
            return helper(nums, target, idx + 1, hasher)
        
        return helper(nums, target, 0, {})