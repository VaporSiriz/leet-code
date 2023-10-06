class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        one_degree_array = []
        for l in matrix:
            one_degree_array += l
            
        start = 0
        end = len(one_degree_array)-1
        while start <= end:
            mid = start + int((end-start)/2)
            print(mid)
            if one_degree_array[mid] == target:
                return True
            if one_degree_array[mid] > target:
                end = mid-1
            elif one_degree_array[mid] < target:
                start = mid+1
        return False