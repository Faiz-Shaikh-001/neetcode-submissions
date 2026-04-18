class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int size = nums.size(); // 4
        if (size <= 1){
            return 0;
        }
        int seenValues[size] = {nums[0],}; // [1]
        int seenValuesCount = 1; // 1
        for(int i=1; i<size; i++){ // 1 - [2], 2 - [3], 3 - [4]
            for(int j=0; j<seenValuesCount; j++){ // 0 - [1], 1 - [2], 2 - [3], 3 - [4]
                if(seenValues[j] == nums[i]){ // false // false, false // false, false false
                    return 1;
                }
            }
            seenValues[seenValuesCount++] = nums[i]; // [1, 2] // [1, 2, 3] // [1, 2, 3, 4]
        }
        return 0;
    }
};
