class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dict = {
            'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
            'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---",
            'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---",
            'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
            'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--",
            'z': "--.."
        }
        ans = set()
        for word in words:
            code = ""
            for letter in word:
                code += morse_dict[letter]
            ans.add(code)
        return len(ans)