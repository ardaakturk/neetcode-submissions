class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_counts = dict()


        for letter in s:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

        for letter in t:
            if letter not in letter_counts:
                return False
            else:
                letter_counts[letter] -= 1

        for k, v in letter_counts.items():
            if v != 0:
                return False

        return True                                                                


