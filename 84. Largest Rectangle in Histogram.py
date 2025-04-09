class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        maxArea = 0
        prev_h = 0
        for i, h in enumerate(heights):
            if h == prev_h:
                continue
            prev_h = h
            index = i

            while stack and stack[-1][0] > h:
                old_height, index =  stack.pop()
                area = (i-index)*old_height
                if area > maxArea:
                    maxArea = area            
            
            if not stack or stack[-1][0] != h:
                stack.append((h, index))

        return maxArea
