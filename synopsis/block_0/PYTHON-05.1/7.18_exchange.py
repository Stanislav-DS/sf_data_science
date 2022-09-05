def exchange(usd=None, rub=None, rate=None):
    not_none = 0
    for arg in (usd, rub, rate):
        if arg is not None:
            not_none += 1
    if not_none == 3:
        raise ValueError('Too many arguments')
    elif not_none == 1:
        raise ValueError('Not enough arguments')

    if usd is None:
        return rub / rate
    elif rub is None:
        return usd * rate
    elif rate is None:
        return rub / usd


print(exchange(rub=1000))