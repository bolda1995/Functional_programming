from functools import reduce

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]
def square_room(d):
    return d.get("length") * d.get("width")

def summa(n1, n2):
    return n1 + n2


print(reduce(summa, map(square_room, rooms)))
