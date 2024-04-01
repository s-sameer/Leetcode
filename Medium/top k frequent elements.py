'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time complexity: O(nlogn)
        # we can use a hashmap to store the count for each num
        store = {}
        res = []
        for num in nums:
            store[num] = 1 + store.get(num, 0)
        # sort the store by the count
        store = sorted(store.items(), key=lambda x: x[1], reverse=True)
        # get the first k elements
        for i in range(k):
            res.append(store[i][0])
        
        return res
    
        # Time complexity: O(n)
        # we'll again use a hashmap to store the count for each num
        store = {}
        res = []
        for num in nums:
            store[num] = 1 + store.get(num, 0)
        # we'll use an array to store the numbers with the index representing the count
        bucket = [[] for _ in range(len(nums) + 1)]
        for val, count in store.items():
            bucket[count].append(val)
        # we'll get the first k elements, we want to start from the back
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
    