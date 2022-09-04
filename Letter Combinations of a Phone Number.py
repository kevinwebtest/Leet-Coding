class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapStrNum = {"2":"abc",
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"}
        if digits == "":
            return []
        before = ['']
        for digit in digits:
            output = []
            for letter in mapStrNum[digit]:
                for prev in before:
                    output.append(prev+letter)
            before = output
        return output
