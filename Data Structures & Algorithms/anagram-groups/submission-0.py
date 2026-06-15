class Solution:
    def compWord(self, s, t):
        CountS = {}
        CountT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i],0)
            CountT[t[i]] = 1 + CountT.get(t[i],0)
        return CountS == CountT
            

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_list = []
        if len(strs) == 1:
            ana_list.append(strs)
            return ana_list
        for word in strs:
            if len(ana_list) == 0:
                ana_list.append([word])
            else:
                Is_added = False
                for catagory in ana_list:
                    if self.compWord(word, catagory[0]):
                        catagory.append(word)
                        Is_added = True
                        break
                if Is_added == False:
                    ana_list.append([word])                 
        return ana_list

        