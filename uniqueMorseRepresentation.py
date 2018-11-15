class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_words = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_encoded_strings = []
        for word in words:
            morse_word = ''
            for ch in word:
                idx = ord(ch) - ord('a')
                morse_word += morse_words[idx]
            morse_encoded_strings.append(morse_word)

        unique = set(morse_encoded_strings)
        return len(unique)


print Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
