N = 1234567
digits = [3, 7, 0]
list(map(lambda x, y:
         print(f'Is the digit {x} included in the number {y}?\n'
               f'Answer: {str(x) in str(y)}'),
         digits, [N] * len(digits)
         ))
