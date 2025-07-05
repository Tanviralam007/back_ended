'''
Group Anagram: Given an array of strings strs, group the anagrams together.
Return a list of groups (each group is a list of anagrams).
'''
from collections import defaultdict

def group_anagram(strs: list[str]) -> list[list[str]]:
    group = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        group[key].append(word)
    
    return list(group.values())

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagram(strs)
    print(result)

if __name__ == "__main__":
    main()

'''
output: [
    ['eat', 'tea', 'ate'], 
    ['tan', 'nat'], 
    ['bat']
]
'''