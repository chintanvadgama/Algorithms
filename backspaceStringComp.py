class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s1 = s2 = ""
        if S == "#" and T == "" or T == "#" and S == "" or T == "#" and S == "#":
            return True
        skip = 0
        for i in range(len(S) - 1, -1, -1):
            if S[i] == "#":
                skip += 1
            elif skip:
                skip -= 1
            else:
                s1 += S[i]
        for j in range(len(T) - 1, -1, -1):
            if T[j] == "#":
                skip += 1
            elif skip:
                skip -= 1
            else:
                s2 += T[j]
        print("s1",s1)
        print("s2",s2)
        return s1 == s2


print(Solution().backspaceCompare("a##c","#a#c"))