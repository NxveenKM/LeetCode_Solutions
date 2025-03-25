class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Sort the list first
        nums.sort()
        
        # Check for duplicates in the sorted list
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        
        return False
