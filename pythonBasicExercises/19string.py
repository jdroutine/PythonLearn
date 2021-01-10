def new_string(str):
    if str.startswith('Is'):
        return str
    return "Is" + str


print(new_string('Damian'))