class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # Case 1: The current subarray is already sorted.
            # The leftmost element must be the smallest in this range.
            
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r) // 2
            # Keep track of the minimum value seen so far
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                # Case 2: Left half is sorted, so the rotation point (and min value must be in the right half.
                l = m+1
            else:
                # Case 3: Right half is sorted, so the min value is either at 'm' (already recorded above) or somewhere in the left half.
                r = m-1
        return res            