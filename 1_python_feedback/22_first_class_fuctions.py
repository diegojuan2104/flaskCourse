def sum(*values):
    total = 0
    for i in values:
        total += i
    return total

def calculate(*values,operator):
    return operator(*values)

result = calculate(32,34, operator = sum)

print(result)

