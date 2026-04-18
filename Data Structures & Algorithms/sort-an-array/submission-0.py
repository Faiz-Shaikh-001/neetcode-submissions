class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            
            sorted_left_half = mergeSort(left_half)
            sorted_right_half = mergeSort(right_half)

            return merge(sorted_left_half, sorted_right_half)

        def merge(sorted_left, sorted_right):
            i, j = 0, 0
            res = []
            while i < len(sorted_left) and j < len(sorted_right):
                if sorted_left[i] < sorted_right[j]:
                    res.append(sorted_left[i])
                    i += 1
                else:
                    res.append(sorted_right[j])
                    j += 1
            
            res.extend(sorted_left[i:])
            res.extend(sorted_right[j:])

            return res
        
        return mergeSort(nums)