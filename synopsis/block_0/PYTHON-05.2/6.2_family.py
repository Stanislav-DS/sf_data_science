family_list = [
    'certificate of a large family',
    'social card',
    'maternity capital',
    'parking permit',
    'tax benefit',
    'reimbursement of expenses',
    "compensation for the purchase of children's goods"
]


def family(*args):
    return list(filter(lambda arg: arg in family_list, args))


print(family('newborn registration',
             'parking permit',
             'maternity capital',
             'tax benefit',
             'medical policy'))