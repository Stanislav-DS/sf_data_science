reg = [('Ivanov', 'Sergej', 24, 9, 1995),
       ('Smith', 'John', 13, 2, 2003),
       ('Petrova', 'Maria', 13, 3, 2003)]

reg_date = filter(lambda col: col[4] >= 2000, reg)
new_reg = map(
    lambda col: (col[0]+' '+col[1][:1]+'.', col[2], col[3], col[4]),
    reg_date
)

new_reg = list(new_reg)

print(new_reg)