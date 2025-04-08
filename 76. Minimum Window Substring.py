class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Step 1: Build a frequency map for characters in t
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        left = 0
        right = 0
        required = len(need)
        formed = 0
        window_counts = {}

        min_len = float("inf")
        min_window = (0, 0)

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in need and window_counts[char] == need[char]:
                formed += 1

            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = (left, right)

                # Try to shrink the window
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in need and window_counts[left_char] < need[left_char]:
                    formed -= 1
                left += 1

            right += 1

        if min_len == float("inf"):
            return ""
        return s[min_window[0]:min_window[1]+1]
