class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_s = "".join(value.lower() for value in s if value.isalnum())
        return stripped_s == stripped_s[::-1]
