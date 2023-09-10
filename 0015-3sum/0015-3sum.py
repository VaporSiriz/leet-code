class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dict_nums = {
            num:0
            for num in nums
        }
        for num in nums:
            dict_nums[num]+=1
            
        set_sums = set()
        for i in range(0, len(nums)-1):
            dict_nums[nums[i]] -= 1
            for j in range(i+1, len(nums)):
                dict_nums[nums[j]] -= 1
                if -(nums[i]+nums[j]) in dict_nums and dict_nums[-(nums[i]+nums[j])]!=0:
                    set_sums.add(tuple(sorted([nums[i], nums[j], -(nums[i]+nums[j])])))
                dict_nums[nums[j]] += 1
            dict_nums[nums[i]] += 1
        return list(set_sums)
        
            