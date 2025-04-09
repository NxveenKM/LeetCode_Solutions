class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        l = SortedList()
        res = 0

        for a in nums:
            i = l.bisect_right(2 * a)
            res += i
            l.add(a) 
        
        return n * (n - 1) // 2 - res
