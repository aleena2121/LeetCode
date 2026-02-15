class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        for i in b:
            if i not in a:
                return -1

        count = len(b) // len(a)
        a_ = a*count
        for i in range(3):
            if b in a_:
                return count
            a_ += a
            count += 1

        return -1