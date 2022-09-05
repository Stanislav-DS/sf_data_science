def syracuse_closure(n):
    """Testing Syracuse hypothesis by closure function."""
    def get_syracuse_seq():
        nonlocal n
        if n == 1:
            pass
        elif n % 2 == 0:
            n //= 2
        else:
            n = (n*3 + 1) // 2

        return n

    return get_syracuse_seq


def syracuse_recursion(n):
    """Testing Syracuse hypothesis by recursion function."""
    if n == 1:
        return 1
    elif n % 2 == 0:
        n //= 2
    else:
        n = (n*3 + 1) // 2

    print(n)
    return syracuse_recursion(n)


def syracuse_generator(n):
    """Testing Syracuse hypothesis by generator function."""
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (n*3 + 1) // 2
        yield n


try:
    num = int(input("Input a natural number for testing Syracuse hypothesis: "))
    if num <= 0:
        raise ValueError
except ValueError:
    print("Error! Wrong input!")
else:
    message = "Syracuse hypothesis for number {} holds!"
    print(syracuse_closure.__doc__)
    get_next_syracuse_num = syracuse_closure(num)
    while True:
        m = get_next_syracuse_num()
        print(m)
        if m == 1:
            print(message.format(num))
            break

    print(syracuse_recursion.__doc__)
    if syracuse_recursion(num) == 1:
        print(message.format(num))

    print(syracuse_generator.__doc__)
    if (syracuse_seq := list(syracuse_generator(num)))[-1] == 1:
        print(*syracuse_seq, message.format(num), sep="\n")