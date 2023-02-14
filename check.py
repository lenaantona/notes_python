import view
import pathlib
import operations as oper

def check_operation(): # проверка на ввод операции
    correct = False
    while not correct:
        try:
            oper = int(view.get_operations())
            if oper in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                correct = True
        except ValueError:
            print('Неверно введена операция, доступны: 0, 1, 2, 3, 4, 5, 6, 7, 8')
    return oper

def check_head(): # проверка на ввод заголовка замекти
    correct = False
    while not correct:
        head = view.get_head()
        if len(head) < 45:
            correct = True
            return head
        else:
            print('Заголовок превышает 45 символов')
    

def check_body(): # проверка на ввод тела замекти
    correct = False
    while not correct:
        body = view.get_body()
        if len(body) < 100:
            correct = True
            return body
        else:
            print('Заголовок превышает 100 символов')

def check_file(): #проверка наличия файла
    path = pathlib.Path('notes.csv')
    if path.is_file() == False:
        return 1
    else:
        return 0

   





