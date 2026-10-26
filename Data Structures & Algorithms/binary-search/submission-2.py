class Solution:
    def search(self, nums: List[int], target: int) -> int:

# put two pointers at the beginning and the end
        l, r = 0, len(nums) - 1 

        while l <= r: #find the middle element
            m = l + ((r-l)//2)
            if nums[m] > target: #check if the middle element is greater than the target or less than the target. According to that, move your pointer.
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1          
        