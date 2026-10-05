class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

#Creating a hashmap so that we can see the diff between target index in prevmap if already exist. Reduces the time complexity of iterating the array and comparing each element again and again.
        prevMap = {}

# we use enumerate to get the index as well. i= index, n = value
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return




