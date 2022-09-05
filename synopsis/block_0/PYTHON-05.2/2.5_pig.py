def saver():
    total = 0
    def adder(arrival):
        nonlocal total
        total += arrival
        return total
    return adder


pig = saver()
print(pig(1))
print(pig(2))
print(pig(100))