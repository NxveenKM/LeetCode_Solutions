class Solution:
    def check(self, nums: List[int]) -> bool:
        count_breaks = 0
        n = len(nums)
        
        for i in range(n):
            # Compare current element with the next (circularly)
            if nums[i] > nums[(i + 1) % n]:
                count_breaks += 1
                
        # At most one break is allowed for the array to be a rotated sorted array
        return count_breaks <= 1
