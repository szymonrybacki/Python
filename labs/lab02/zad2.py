def round_numbers(numbers: list[int], threshold: int) -> list[int]:
    def round_down(num: int) -> int:
        return num - (num % 10)
    def round_up(num: int) -> int:
        return ((num + 9) // 10) * 10

    result = []
    for n in numbers:
        if n < threshold:
            result.append(round_down(n))
        else:
            result.append(round_up(n))
    return result

print(round_numbers([12, 25, 3, 41, 55, 61, 27, 18, 49, 1], 20))  # [10, 30, 0, 50, 60, 70, 30, 10, 50, 0]