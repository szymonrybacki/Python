def group_words_by_length(words: list[str]) -> dict:
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result

print(group_words_by_length(['ala', 'ma', 'kota', 'a', 'kot', 'ma', 'ale']))  # {3: ['ala', 'ma', 'kot', 'ale'], 4: ['kota']}