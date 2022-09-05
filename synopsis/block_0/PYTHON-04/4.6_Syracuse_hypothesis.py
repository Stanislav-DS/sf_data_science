n = 19  # задаём число
# создаём бесконечный цикл
print(f"Testing the Syracuse hypothesis for a number {n}")
while True:
    if n == 1:  # если результат равен 1,
        print('Syracuse hypothesis holds')  # выводим утвердительное сообщение
        break
    elif n % 2 == 0:
        print(f"{n} // 2 = {n // 2}")
        n //= 2
    else:
        print(f"({n}*3 + 1) // 2 = {(n*3 + 1) // 2}")
        n = (n*3 + 1) // 2


"""
Testing the Syracuse hypothesis for a number 19
(19*3 + 1) // 2 = 29
(29*3 + 1) // 2 = 44
44 // 2 = 22
22 // 2 = 11
(11*3 + 1) // 2 = 17
(17*3 + 1) // 2 = 26
26 // 2 = 13
(13*3 + 1) // 2 = 20
20 // 2 = 10
10 // 2 = 5
(5*3 + 1) // 2 = 8
8 // 2 = 4
4 // 2 = 2
2 // 2 = 1
Syracuse hypothesis holds
"""