from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        map_fr=defaultdict(int)
        for i in nums:
            map_fr[i] += 1
        sor= sorted(map_fr.items(),key=lambda x : x[1],reverse=True)
        result=[]
        for j in range(k):
            result.append(sor[j][0])
        return result