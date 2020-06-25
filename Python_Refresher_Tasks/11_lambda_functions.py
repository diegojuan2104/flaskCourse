#print((lambda x, y: x + y)(5,7))

sequence = [1,23,12,45]

#list comprenhensions 
doubled = [(lambda x: x*2)(x) for x in sequence]
doubled = list(map(lambda x: x*2,sequence))

print(doubled)