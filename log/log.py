from datetime import datetime as dt


def my_log(text):
    time = dt.now().strftime("%H:%M:%S")
    log_string = f"{time}; {text}\n"
    with open('log\phonebook.log', 'a', encoding='utf-8') as file:
        file.write(log_string)
