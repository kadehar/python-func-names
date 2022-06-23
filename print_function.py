def print_info_about(*functions):
    for fun in functions:
        name = fun.__name__
        args_names = fun.__code__.co_varnames

        if len(args_names) == 0:
            args = '[]'
        else:
            args = f'[{", ".join(args_names)}]'

        print(f'{name}:{args}')
