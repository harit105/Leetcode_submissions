class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: 'l' at the start and 'r' at the end
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]
            # If the sum is too large, decrement the right pointer to decrease the sum
            if currSum > target:
                r -= 1
            # If the sum is too small, increment the left pointer to increase the sum
            elif currSum < target:
                l += 1
            else:
            # Found the pair: convert to 1-based indices as required
                return [l+1, r+1]
        # Fallback return (problem guarantees exactly one valid solution)
        return []       
#Brute force approach: you basically compare each number with all the other numbers present in the array.
#[1,3,4,5,7,10,11] Target: 9
#1 + 3, 1 + 4.....  1+10 = 11 which is greater than 9 so we do not check 11 or 10 again when comparing other values.
# move to 3
#3+4,3+5, 3+7 = 10 so 7 is out as well. Notice the pattern we repeat this again and again till we find the target, n.n

#instead we keep two pointers, first indice and last indice and get the sum of those two and based on the result we identify whether we want to move left or right.