public class Solution {
    public int RemoveDuplicates(int[] nums) {
        if (nums.Length == 0) return 0;
        int cur = 0;
        for (int i = 1; i < nums.Length; i++){
            if (nums[i] != nums[cur]){
                cur++;
                nums[cur] = nums[i];
            }
        }
        return cur + 1;
    }
}