class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            email = ""
            index_at = s.index("@")
            email += s[0].lower()
            email += "*"*5
            email += s[index_at-1:].lower()
            return email
        else:
            phone_number = ""
            s = s.replace('(',"").replace(")","").replace("-","").replace(" ","").replace("+","")
            if len(s) > 10:
                phone_number += "+"
                phone_number += "*"*(len(s)-10)
                phone_number += "-"
            phone_number += "***-"*2
            phone_number += s[len(s)-4:]
            return phone_number
