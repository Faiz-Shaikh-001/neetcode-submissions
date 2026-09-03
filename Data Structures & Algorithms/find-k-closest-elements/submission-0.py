class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def binarySearch(arr, x):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = l + (r-l) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        
        elementAt = binarySearch(arr, x)
        l, r = elementAt - 1, elementAt

        while r-l-1 < k:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            else:
                if x - arr[l] <= arr[r] - x:
                    l -= 1
                else:
                    r += 1
        return arr[l+1:r]