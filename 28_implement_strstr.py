class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        indices = [i for i, x in enumerate(haystack) if x == needle[0]]
        needle_indices = [i for i in indices if haystack[i:i+len(needle)] == needle]
        if len(needle_indices)>0:
            return needle_indices[0]
        else:
            return -1