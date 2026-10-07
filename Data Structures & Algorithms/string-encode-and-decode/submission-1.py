class Solution:

    """
    ["Hello", "World"] -> 5#Hello5#World
    [] ->
    [""] -> 0#
    ["", ""] -> 0#0#
    """

    def encode(self, strs: list[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        return "".join(res)


    """
    5#Hello5#World -> ["Hello", "World"]
    "" -> []
    0# -> [""]
    0#0# -> ["", ""]
    """
    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            s_len = int(s[i:j])
            i = j + 1 # The beginning index of the next word
            res.append(s[i:i+s_len])
            i = i + s_len
        return res