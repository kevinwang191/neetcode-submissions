class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for word in strs:
            long = len(word)
            final = final + str(long) + "#" + word
        return final

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            start = j+1
            word = s[start:start+length]
            res.append(word)
            i = start+length
        return res
        


            