class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water_container = -1
        while l < r:
            height = min(heights[l], heights[r])
            max_water_container = max(max_water_container, (r-l) * height)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water_container
