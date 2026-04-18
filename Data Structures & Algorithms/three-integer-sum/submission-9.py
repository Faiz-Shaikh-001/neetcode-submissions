class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        length = len(sorted_nums)
        result = []
        hash_map = dict()
        
        for i in range(length):
            curr_val = sorted_nums[i]
            required_val = -1 * curr_val
            hash_map[curr_val] = []
            j = 0
            k = length-1
            while j < k:    
                if j != i and k != i:
                    new_sum = sorted_nums[j] + sorted_nums[k]
                    if new_sum == required_val:
                        if [sorted_nums[j], sorted_nums[k]] not in hash_map[curr_val]:
                            hash_map[curr_val].append([sorted_nums[j], sorted_nums[k]])
                        j+=1
                    elif new_sum < required_val:
                        j+=1
                    elif new_sum > required_val:
                        k-=1
                else:
                    if j == i:
                        j += 1
                    elif k == i:
                        k-=1
        
        for key, val in hash_map.items():
            if len(val) == 0:
                continue
            else:
                for arr in val:
                    new_arr = sorted([key, arr[0], arr[1]])
                    if new_arr not in result:
                        result.append(new_arr)
                    
        return result


        