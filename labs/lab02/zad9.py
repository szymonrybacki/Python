def unique_permutations(elements: list) -> list:
    result = []
    
    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return
            
        used = set()  # Śledzenie elementów już użytych na tym poziomie
        
        for i in range(len(remaining)):
            if remaining[i] in used:
                continue
                
            used.add(remaining[i])
            
            current.append(remaining[i])
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(current, new_remaining)
            current.pop()
    
    backtrack([], elements)
    return result

print(unique_permutations([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]