class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # This dict will keep the sorted str as a key, and list of its anagrams
        """
        {"act" = ["act", "cat"],
         "opst" = ["stop", "pots", "tops"]}
        """
        anagrams_dict: dict[str, list] = dict()

        for str in strs: # O(n)
            sorted_str = "".join(sorted(str)) # O(mlogm)
            if sorted_str in anagrams_dict:
                anagrams_dict[sorted_str].append(str)
            else:
                anagrams_dict[sorted_str] = []
                anagrams_dict[sorted_str].append(str)     

        anagram_lists = []
        for anagram_list in anagrams_dict.values():
            anagram_lists.append(anagram_list)

        return anagram_lists








        
            
            




            


        