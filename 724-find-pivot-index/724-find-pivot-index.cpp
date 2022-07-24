class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        if (nums.size() == 0 )
            return -1;
        int ts=0,ls=0;
        for(auto x:nums)
            ts+=x;
        for(int i=0;i<nums.size();i++){
           if(ls==(ts-nums[i]))
               return i;
           else{
               ls+=nums[i];
               ts-=nums[i];
           } 
        }
    return -1;   
    }
};