class Solution:
    def romanToInt(self, s: str) -> int:
        total=0
        for num in range(len(s)):
            if s[num] == "I":
                total+=1
            elif s[num] == "V":
                if ((num-1!=-1) & (s[num-1] == "I")):
                    total+=3
                else:
                    total+=5
            elif s[num] == "X":
                if ((num-1!=-1) & (s[num-1] == "I")):
                    total+=8
                else:
                    total+=10
            elif s[num] == "L":
                if ((num-1!=-1) & (s[num-1] == "X")):
                    total+=30
                else:
                    total+=50
            elif s[num] == "C":
                if ((num-1!=-1) & (s[num-1] == "X")):
                    total+=80
                else:
                    total+=100
            elif s[num] == "D":
                if ((num-1!=-1) & (s[num-1] == "C")):
                    total=total+300
                else:
                    total+=500
            elif s[num] == "M":
                if ((num-1!=-1) & (s[num-1] == "C")):
                    total+=800
                else:
                    total+=1000
        return total
