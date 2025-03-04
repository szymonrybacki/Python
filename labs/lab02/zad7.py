def most_frequent_element(data: list):
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1

    most_common = None
    highest_count = 0
    for item, count in frequency.items():
        if count > highest_count:
            most_common = item
            highest_count = count
    return most_common

print(most_frequent_element([1, 2, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6]))  # 1