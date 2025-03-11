def najdluzszy_wspolny_podciag(s1, s2):
    # Tworzenie tablicy dp do przechowywania długości LCS
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Wypełnianie tablicy dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Odtwarzanie podciągu
    i, j = m, n
    lcs = []
    
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Podciąg jest ułożony od końca, więc go odwracamy
    return ''.join(reversed(lcs))

# Testy
print(najdluzszy_wspolny_podciag("ABCDEF", "ACBEF"))  # ABEF
print(najdluzszy_wspolny_podciag("XMJYAUZ", "MZJAWXU"))  # MJAU
print(najdluzszy_wspolny_podciag("hello", "world"))  # "l" lub "o"