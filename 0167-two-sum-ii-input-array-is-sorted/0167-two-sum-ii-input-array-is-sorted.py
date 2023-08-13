class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict_numbers = {
            number:index for index, number in enumerate(numbers)
        }
        for index, number in enumerate(numbers):
            if target-number in dict_numbers:
                return [index+1, dict_numbers[target-number]+1]