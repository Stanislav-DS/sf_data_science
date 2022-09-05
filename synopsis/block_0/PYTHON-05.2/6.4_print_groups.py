def group_gen(n=3):
    while True:
        for i in range(1, n+1):
            yield i


def print_groups(users):
    n_group = group_gen()
    groups = zip(users, n_group)
    for entry in groups:
        print("{} in group {}".format(entry[0], entry[1]))


users = ['Smith J.', 'Petrova M.', 'Lubimov M.', 'Holov J.']
print_groups(users)