from datetime import datetime as d
import check as ch

def get_start(): # приветствие
    return print('Вас приветствует программа заметок!')

def get_operations(): # получение операции
    return input('Доступны следующие операции:\n 1 - создание заметки,\n 2 - добавление, 3 - просмотр списка заметок,\n 4 - поиск по всей заметке, 5 - поиск по id, 6 - поиск записи по дате,\n 7 - редактирование, 8 - удаление \n 0 - завершение программы \n')  

def get_head(): #получение заголовка заметки
    return input('Введите заголовок замекти, но не больше 45 символов: ')

def get_body(): #получение тела заметки
    return input('Введите тело заметки, но не больше 100 символов: ')  

def print_notes(data): #ввыод на консоль
    print('Результат:\n')
    for i in data:
        print(str(i)+'\n')      

def get_notes(): #получение данных замекти с консоли
    time = d.now().strftime('%d/%m/%y %H:%M')
    str_head = ch.check_head()
    str_body = ch.check_body()
    str_notes = str_head + ';' + str_body + ';' + time  
    return str_notes 

def get_id(): #получение id
    return input('Введите id записи замекти: ') 

def get_searched(): #получение строки запроса
    return input('Введите, что искать:  ')          

def get_data():
    return input ('Введите дату в формате день/месяц/год(2 цифры): ')    
