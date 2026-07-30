class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        for word in strs:
            encoded.append(str(len(word)))
            encoded.append('#')
            encoded.append(word)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':        # find the separator after the length
                j += 1
            length = int(s[i:j])      # parse length
            j += 1                    # move past '#'
            decoded.append(s[j:j+length]) # grab exactly length chars
            i = j + length            # move to next chunk
        return decoded
