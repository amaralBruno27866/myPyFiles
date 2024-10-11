class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]: # The function that will return the indexes of the numbers that sum to the target
    hasher = {} # The variable that will store the hash table
    for idx, i in enumerate(nums): # This loop will iterate through the list of numbers
      if hasher.get(i) is not None: # Here we check if the number is already in the hash table
        return [hasher.get(i), idx] # If it is, we return the indexes of the numbers that sum to
      hasher[target - i] = idx # If the number is not in the hash table, we add the difference between the target and the number as the key and the index as the value