class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Initialize empty count hashmap and bucket list freq with seven empty lists or the length of the number of elements +1
            count = {}
            freq = [[] for i in range(len(nums) + 1)]
#Update count of all the numbers present in the array nums
            for n in nums:
                count[n] = 1 + count.get(n,0)
#Populate bucket: number 1 has count 1, append 1 to freq[1]
#Populate bucket: number 2 has count 2, append 2 to freq[2]
            for n, c in count.items():
                freq[c].append(n)
#Initialize result array and prepare to iterate through freq buckets in reverse order
            res = []

            for i in range(len(freq) - 1, 0 , -1):
                for n in freq[i]:
                    res.append(n)
                    if len(res)== k:
                        return res

        