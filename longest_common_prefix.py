class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(x) for x in strs])
        prefixes = [[x[:i] for x in strs] for i in range(1,min_length+1)]
        print(prefixes)
        same_prefixes = [list(set(x)) for x in prefixes if len(set(x))==1]
        flattened = [item for sublist in same_prefixes for item in sublist]
        
        if len(flattened)==0:
            return ""
        else:
            return max(flattened, key=len)
        
