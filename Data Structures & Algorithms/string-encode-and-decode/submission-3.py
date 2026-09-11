class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []
        for string in strs:
            num = len(string)
            new_str = str(num) + '#' + string
            arr.append(new_str)

        return "".join(arr)

    # 7#Hello4#5#World
    def decode(self, s: str) -> List[str]:
        ans =  []
        n = len(s)

        i, j = 0, 0
        while j < n:
            while j < n and s[j] != '#':
                j += 1
            num = int(s[i:j])
            i = j + 1
            j = i + num

            string = s[i:j]
            ans.append(string)
            i = j

        return ans
            


            


        


