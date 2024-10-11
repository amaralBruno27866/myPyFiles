class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]: # The function that will return the indexes of the numbers that sum to the target
    hasher = {} # The variable that will store the hash table

    for idx, i in enumerate(nums): # This loop will iterate through the list of numbers
      if hasher.get(i) is not None: # Here we check if the number is already in the hash table
        return [hasher.get(i), idx] # If it is, we return the indexes of the numbers that sum to
      
      hasher[target - i] = idx # If the number is not in the hash table, we add the difference between the target and the number as the key and the index as the value

# Using a solution by recursive function
class Solution2:
  def two_sum(self, nums: list[int], target: int) -> list[int]: # The function that will return the indexes of the numbers that sum to the target
    def helper(nums, target, idx, hasher): # The recursive function that will help us find the indexes of the numbers that sum to the target
      if idx >= len(nums): # If the index is greater than or equal to the length of the list, we return an empty list
        return [] # This is the base case of the recursive function
      
      current = nums[idx] # The current number in the list

      if current in hasher: # If the current number is in the hash table, we return the indexes of the numbers that sum to the target
        return [hasher[current], idx] # This is the base case of the recursive function
      
      hasher[target - current] = idx # If the current number is not in the hash table, we add the difference between the target and the current number as the key and the index as the value

      return helper(nums,target, idx + 1, hasher) # We call the recursive function with the next index
    
    return helper(nums, target, 0, {}) # We call the recursive function with the initial index and an empty hash table