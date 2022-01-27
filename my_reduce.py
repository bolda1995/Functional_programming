"""
Создайте функцию myreduce, которая будет работать так же как и оригинальная reduce.
"""

def myreduce(function, arg):

    result = function(arg[0], arg[1])

    for el in range(3, len(arg) + 1):
        result = function(result, el)

    return result


def main():

    lala = [1, 2, 3, 4]
    print(myreduce(lambda x, y: x + y, lala))

if __name__ == "__main__":
    main()