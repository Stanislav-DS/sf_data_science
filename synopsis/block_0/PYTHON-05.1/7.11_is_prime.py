def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return False if num == 1 else True


print(is_prime(13))

