class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (-x[0],x[1]))
        countweak = 0
        maxsecondnum = 0
        for _, secondnum in properties:
            if maxsecondnum > secondnum:
                countweak += 1
            else:
                maxsecondnum = secondnum
        return countweak
