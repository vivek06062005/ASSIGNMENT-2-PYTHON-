def count_matching_characters(s1, s2):
    matches = sum(1 for a, b in zip(s1, s2) if a == b)
    return matches
S1 = "what"
S2 = "watch"
print(count_matching_characters(S1, S2))
