people = [
    {"sex": "m", "age": 12},
    {"sex": "w", "age": 12},
    {"sex": "m", "age": 15},
    {"sex": "m", "age": 20},
    {"sex": "m", "age": 13},
    {"sex": "m", "age": 27},
    {"sex": "w", "age": 31},
    {"sex": "m", "age": 17},
    {"sex": "w", "age": 17},
    {"sex": "m", "age": 12},
    {"sex": "m", "age": 42},
    {"sex": "w", "age": 25}
]
def sort_people(d):
    bio = d.get('sex'), d.get('age')
    if bio[0] == 'm' and 20 <= bio[1] <= 30:
        return True
my_people = filter(sort_people, people)