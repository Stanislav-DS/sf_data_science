random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]
max_elem = []
max_row = 0
for row in random_matrix:
    max_row = row[0]
    for elem in row:
        if max_row < elem:
            max_row = elem
    max_elem.append(max_row)
print("Maximums in rows ", max_elem)

# Maximums in rows  [9, 5, 8]