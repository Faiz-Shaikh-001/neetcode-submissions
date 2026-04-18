class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
            
        from collections import defaultdict
        hash_map = defaultdict()
        for num in nums:
            if num in hash_map:
                continue
            hash_map[num] = hash_map.get(num, 0) + 1
            current_num = num
            while True:
                if (current_num-1) not in hash_map.keys() and (current_num-1) not in nums:
                    break
                elif (current_num - 1) in hash_map.keys():
                    hash_map[num] += hash_map[current_num-1]
                    break
                elif (current_num - 1) not in hash_map.keys() and (current_num - 1) in nums:
                    hash_map[num] += 1
                    current_num -= 1
                else:
                    break
        return max(hash_map.values())
            # initialize the hash map keys with value 1
            # { 2: 1, 20: 1, 4: 1, 10: 1, 3: 1, 5: 1}
            


