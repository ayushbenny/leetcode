class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        new_dict1 = {}
        new_dict2 = {}

        is_iso = True  # assume they are isomorphic unless proven otherwise

        for ch1, ch2 in zip(s, t):
            # check if mapping already exists in s→t
            if ch1 in new_dict1 and new_dict1[ch1] != ch2:
                is_iso = False
                break
            # check if mapping already exists in t→s
            if ch2 in new_dict2 and new_dict2[ch2] != ch1:
                is_iso = False
                break
            # store mapping both ways
            new_dict1[ch1] = ch2
            new_dict2[ch2] = ch1
        return is_iso