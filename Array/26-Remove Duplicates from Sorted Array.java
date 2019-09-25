class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int cur = 0;
        for (int i = 1; i < nums.length; i++){
            if (nums[i] != nums[cur]){
                cur++;
                nums[cur] = nums[i];
            }
        }
        return cur + 1;
    }
}