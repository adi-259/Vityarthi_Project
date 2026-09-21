def count_items(values):
    total = 0
    for value in values:
        total += value
    return total

def maximum(values):
    if not values:
        return None
    largest = values[0]
    for value in values[1:]:
        if value > largest:
            largest = value
    return largest

def selection_sort(values):
    data = values.copy()
    for i in range(len(data)):
        smallest = i
        for j in range(i + 1, len(data)):
            if data[j] < data[smallest]:
                smallest = j
        data[i], data[smallest] = data[smallest], data[i]
    return data
