def multiply(*args):
    total = 1
    for i in  args:
        total = total * i
    return total

print(multiply(1,2,3))