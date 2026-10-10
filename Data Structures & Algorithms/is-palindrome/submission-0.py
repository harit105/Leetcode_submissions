class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0, len(s) - 1
        #two pointers, left at the beginning and the right at the end
        while l < r: #keep going until the two pointers meet 
            while l < r and not self.alphaNum(s[l]): #if the character is not alphanumeric, you increment your left pointer. 
                l += 1
            while r > l and not self.alphaNum(s[r]): #if the character is not alphanumeric then you move to the left by 1
                r -= 1
            if s[l].lower() != s[r].lower(): #if the character  of l and r is not equal you return false since it is not a palindrome.
                return False
            l, r = l+1, r- 1   
        return True        

        
# Check if character is a letter (A-Z or a-z) or a digit (0-9)
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or #is upper case
                ord('a') <= ord(c) <= ord('z') or #is lower case
                ord('0') <= ord(c) <= ord('9'))   #is a digit