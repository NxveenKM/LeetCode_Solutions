class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        prefix_sm = 0
        dct = defaultdict(int)
        cnt = 0
        dct[0] = 1
        for i, n in enumerate(nums):
            prefix_sm += n
            if prefix_sm-k in dct:
                cnt += dct[prefix_sm-k]
            dct[prefix_sm] += 1
        return cnt
