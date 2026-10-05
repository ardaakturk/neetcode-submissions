from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict: dict[str, list] = defaultdict(list)

        for word in strs: # O(n) - n is the number of strings
            sorted_str = "".join(sorted(word)) # O(mlogm)
            anagrams_dict[sorted_str].append(word)     

        return list(anagrams_dict.values())








        
            
            




            


        