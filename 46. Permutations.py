class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        used = [False] * len(nums)
        backtrack([], used)
        return result
