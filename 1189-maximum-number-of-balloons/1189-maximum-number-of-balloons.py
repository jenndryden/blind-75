class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {'b' : 0, 'a' : 0, 'l' : 0, 'o' : 0 , 'n': 0}
        
        for letter in text:
            if letter in letters:
                letters[letter] += 1

        letters['l']//=2 
        letters['o']//=2
        
        return(min(letters.values()))