def transposition_cipher(text: str, key: int) -> str:
    if key > len(text):
        return text
    chars = list(text)
    for i in range(0, len(chars), key):
        if i + key < len(chars):
            chars[i], chars[i + key] = chars[i + key], chars[i]
    return "".join(chars)

print(transposition_cipher('ala ma kota', 2))  # 'alm  aokata'
print(transposition_cipher('ala ma kota', 20))  # 'ala ma kota'
