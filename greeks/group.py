def group_by_parity(arr):
    return {i % 2: [x for x in arr if x % 2 == i] for i in range(2)}

print(group_by_parity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

