class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == "-":
            s_inv = "-" + s[1:][::-1]
        else:
            s_inv = s[::-1]
        ret = int(s_inv)
        if ret<-2**31 or ret>2**31-1:
            return 0
        else:
            return ret
