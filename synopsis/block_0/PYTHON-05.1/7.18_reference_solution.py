def exchange(usd=None, rub=None, rate=None):
    check = [usd, rub, rate].count(None)
    err_lst = [
        'Too many arguments',
        None,
        'Not enough arguments',
        'Not enough arguments'
    ]
    if check != 1:
        raise ValueError(err_lst[check])

    if usd is None:
        usd = rub / rate
        return usd
    if rub is None:
        rub = usd * rate
        return rub
    if rate is None:
        rate = rub / usd
        return rate


exchange(usd=None, rub=None, rate=None)