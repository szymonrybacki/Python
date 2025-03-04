def readability_score(text: str) -> float:
    import re

    # Podział na zdania - usuwamy puste wpisy
    sentences = re.split(r'[.?!]', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return 0.0

    # Podział na słowa
    words = text.split()
    if not words:
        return 0.0

    # Średnia liczba słów w zdaniu
    avg_words_per_sentence = len(words) / len(sentences)

    # Funkcja licząca sylaby (przykładowe uproszczenie)
    def count_syllables(word: str) -> int:
        vowels = 'aeiouyAEIOUY'
        return sum(ch in vowels for ch in word)

    # Obliczenie łącznej liczby sylab
    total_syllables = sum(count_syllables(w) for w in words)

    # Średnia liczba sylab w słowie
    avg_syllables_per_word = total_syllables / len(words)

    # Prosty wskaźnik łączący obie średnie (przykładowy)
    return avg_words_per_sentence + avg_syllables_per_word


print(readability_score('Ala ma kota. Kot ma Aleksandrę. Ignacy. Wacław! '))  # 3.875