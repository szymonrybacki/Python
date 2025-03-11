def czy_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Testy
assert czy_anagram("kot", "tok")
assert not czy_anagram("kot", "toki")