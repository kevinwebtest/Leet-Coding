class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = string.ascii_lowercase
        morsemap = dict(zip(alpha, morse_code))
        morse = ""
        morsewords = []
        
        for word in words:
            morse = ""
            for c in word:
                morse += morsemap[c]
            morsewords.append(morse)
        
        unique = []
        for i in morsewords:
            if i not in unique:
                unique.append(i)
        return len(unique)
                
