from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_gram=defaultdict(list)
        result=[]
    
        for i in strs:
            sort_s=tuple(sorted(i))
            map_gram[sort_s].append(i)
        for v in map_gram.values():
            result.append(v)
        return result
       
        
 

