def sort_sides(sides=None):
    sides.sort(key=lambda x: (x[0]**2 + x[1]**2) ** (1/2))
    return sides


print(sort_sides([(3, 4), (1, 2), (10, 10)]))
