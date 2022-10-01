import gui.gui as gui
import actions.actions as action


def work():
    p = gui.path_file()
    print(p)
    print('Что желаем сделать:\n\
    1 - Прочитать справочник;\n\
    2 - Записать справочник;\n\
    3 - Поиск в справочнике;\n\
    4 - Удалить запись;\n\
    5 - Экспорт в csv;\n\
    6 - Экспорт в json')
    act = int(input('Выберие действие --> '))
    if act == 1:
        data = action.export_data(p)
        action.print_file(data)
        # actions.read_file(p)
    elif act == 2:
        action.write_in_file(p)
    elif act == 3:
        action.new_find(p)
        # actions.find_in_file(p)
    elif act == 4:
        action.delete_in_file(p)
    elif act == 5:
        action.export_csv(p)
    elif act == 6:
        action.export_json(p)
