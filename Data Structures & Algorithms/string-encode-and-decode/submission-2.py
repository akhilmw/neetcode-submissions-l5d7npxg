class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for s in strs:
            string += str(len(s)) + '/' + s
        
        return string
        
    # neet4code4love4you3  
    # 4#neet4#code4#love3#you  

    def decode(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        i = 0
        while i < n:
            j = i
            while s[j] != '/':
                j+= 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j
        

        return ans


            



        



