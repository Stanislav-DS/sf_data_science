# Мои усовершенстования примера из теории.
# В изначальном варианте ошибка ValueError не обрабатывалась,
# хотя строки присвоения значений переменным, вызывающие эту ошибку,
# были включены в конструкцию try...except, что противоречит общим
# рекомендациям PEP8!
try:
    print("Before exception ValueError")
    a = int(input("a: "))
    b = int(input("b: "))
except ValueError:
    print("After exception ValueError")
else:
    try:
        print("Before exception ZeroDivisionError")
        c = a / b
    except ZeroDivisionError:
        print("After exception ZeroDivisionError")
    else:
        print(c)
        print("Everything's fine!")
finally:
    print("Finally finished!")

print("After After exception")