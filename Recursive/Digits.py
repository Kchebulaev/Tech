
def returnDigits(digit):
    if digit < 10:
        return 1
    else:
        return 1 + returnDigits(digit/10)


digits = [15, 105, 15105]

for digit in digits:
    print returnDigits(digit)