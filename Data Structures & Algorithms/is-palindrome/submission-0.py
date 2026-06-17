import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.replace(" ","").lower().translate(str.maketrans("", "", string.punctuation))
        fp = 0
        bp = -1
        
        for i in range((len(new_s)+1)//2):
            if new_s[bp-i] != new_s[fp+i]:
                return False


        return True