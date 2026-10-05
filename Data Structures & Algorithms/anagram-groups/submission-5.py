from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict: dict[tuple(int), list] = defaultdict(list)

        for word in strs: # O(n) - n is the number of strings
            freq_list = [0] * 26
            for l in word:
                freq_list[ord(l) - ord('a')] += 1
            anagrams_dict[tuple(freq_list)].append(word)     

        return list(anagrams_dict.values())








        
            
            




            


        