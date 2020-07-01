from typing import List

def list_avg(sequence: List):
    return sum(sequence)/len(sequence)

list = [1234,3432,2332]

print(list_avg(list))