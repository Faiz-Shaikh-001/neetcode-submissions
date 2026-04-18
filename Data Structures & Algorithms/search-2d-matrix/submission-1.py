class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        
        while l <= r:
            mid = (l + r) // 2

            if self.search(matrix[mid], target):
                return True
            else:
                if matrix[mid][0] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False

    def search(self, arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l + r) // 2
            if target == arr[mid]:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
            
