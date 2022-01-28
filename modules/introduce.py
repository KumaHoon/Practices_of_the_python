# introduce.py


def join_names(names):
    name_string = ''

    for index, name in enumerate(names):
        if index > 0 and len(names) > 2:
            name_string += ','
        if index > 0:
            name_string += ' '
        if index == len(names) - 1:
            name_string += 'and '
        name_string += name
    return name_string

def introduce(title, names):
    print(f'{title}: {join_names(names)}')

introduce('The Three Stooges', ['Moe', 'Larry', 'Shemp'])
introduce('The Three Stooges', ['Larry', 'Curly', 'Moe'])

introduce('Teenage Mutant Ninja Turtles ', ['Donatello', 'Raphael', 'Michelangelo', 'Leonardo'])
