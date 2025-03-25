class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}  # Dictionary to store number and its index
        
        for index, num in enumerate(nums):
            complement = target - num  # Calculate the complement
            if complement in num_to_index:
                return [num_to_index[complement], index]  # Return indices of the two numbers
            num_to_index[num] = index  # Store the index of the current number
        
        return []  # In case there is no solution, though the problem guarantees one
