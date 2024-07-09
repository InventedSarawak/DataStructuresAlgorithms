class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = nums.size();
        int count = 1;
        for(int i = 1; i < len; i ++) {
            if(nums[i - 1] != nums[i]) nums[count ++] = nums[i];
        }
        return count;
    }
};