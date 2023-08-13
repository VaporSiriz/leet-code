class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l<=r:
            sum_of = numbers[l] + numbers[r]
            if sum_of == target:
                return [l+1, r+1]
            
            if sum_of < target:
                l += 1
            elif sum_of > target:
                r -= 1