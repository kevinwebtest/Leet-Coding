class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        nonDuplicate = {}
        for path in paths:
            data = path.split(" ")
            for text in data[1:]:
                number, content = text.split("(")
                content = content[:-1]
                fullpath = data[0]+'/'+number
                nonDuplicate[content] = nonDuplicate.get(content,[]) + [fullpath]

        return [nonDuplicate[key] for key in nonDuplicate if len(nonDuplicate[key])>1]
