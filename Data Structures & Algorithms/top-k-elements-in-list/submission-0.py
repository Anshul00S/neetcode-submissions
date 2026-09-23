class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        arr = []
        res = []

        for num in nums:
            counts[num] += 1

        for num, freq in counts.items():
            arr.append((freq, num))
        
        arr.sort(reverse= True)

        for i in range(k):
            res.append(arr[i][1])

        return res

