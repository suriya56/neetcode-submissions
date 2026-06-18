class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=[]
        cas=s.lower()
        for i in cas:
            if 'a'<= i <='z' or '0'<= i <='9':
                temp.append(i)
        s_1="".join(temp)
        print(s_1)
        if s_1 == s_1[::-1]:
            return True
        else:
            return False