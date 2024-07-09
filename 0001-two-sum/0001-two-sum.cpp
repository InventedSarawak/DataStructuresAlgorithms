class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> soln(2, -1);
        int len = nums.size();
        for(int i = 0; i < len; i ++) {
            for(int j = i + 1; j < len; j ++) {
                if(nums[i] + nums[j] == target && i != j) {
                    soln[0] = i;
                    soln[1] = j;
                    return soln;
                }
            }
        }
        return soln;
    }
};