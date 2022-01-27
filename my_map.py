def mymap(function, *args):

    result = []
    min_len_args = min([len(arg) for arg in args])

    for i in range(min_len_args):
        func_args = []

        for arg in args:
            func_args.append(arg[i])

        result.append(function(*func_args))

    return list(result)


def main():
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5]

    result = mymap(lambda x, y: x + y, numbers1, numbers2)
    print(result)
if __name__ == "__main__":
    main()