class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = left = 0
        right = len(height) - 1

        while right - left > 0:
            res = max(min(height[left], height[right]) * (right - left), res)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(Solution().maxArea(height=height))
