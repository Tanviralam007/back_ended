# valid anagram: Given two strings s and t, return True if t is an anagram of s, and False otherwise

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    
    for ch in t:
        if ch not in count: 
            return False
        count[ch] = count[ch] - 1
        if count[ch] < 0: 
            return False
    
    return True

