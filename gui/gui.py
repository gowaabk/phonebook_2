def add_contact():
    surname = input('Введите фамилию: -- >')
    name = input('Введите имя контакта: --> ')
    about = input('Введите описание контакта: --> ')
    number = input('Введите номер контакта: --> ')
    col = surname + ',' + name + ','+about + ',' + number + ';'
    return col


def find_contact():
    name = input('Введие имя контакт: ')
    return name


def action():
    act = input('Введите действие: ')
    return act


def path_file():
    path = 'db\phone.txt'  # input('Введите путь: ')
    return path

