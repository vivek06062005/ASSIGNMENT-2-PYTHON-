from collections import defaultdict
def group_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        anagrams[tuple(sorted(s))].append(s)
    return list(anagrams.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(strs)
print(output)
