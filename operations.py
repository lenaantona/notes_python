from datetime import datetime as d
import check as ch

def creat_notes(str_notes): # создание заметки
    head ='id;head;body;datatime'
    str_notes = '0;' + str_notes
    with open ("notes.csv", 'a', encoding='utf-8') as data:
            data.writelines(head + '\n' + str_notes + '\n')
    print('Заметка успешна создана файл notes.csv\n\n')    

def notes_parse(): #парсит файл заметок
    temp_notes = list()
    temp_notes_splited = list()

    with open ("notes.csv", 'r', encoding='utf-8') as data:
        for line in data: temp_notes.append(line)
    
    for i in temp_notes:
        temp_list = i.split(';')
        temp_list[-1] = temp_list[-1][:-1:] 
        temp_notes_splited.append(temp_list)
    
    return temp_notes_splited

def add_notes(notes_data): #добавление записи в конец файла
    idcount = len(notes_parse())-1
    notes_data = str(idcount) + ';' + notes_data + '\n'
    with open ("notes.csv", 'a', encoding='utf-8') as data:
            data.writelines(notes_data)
    print('Заметка успешно добавлена \n\n')   

def search_notes(str_notes, oper): #поиск записи заметки по любому словосочетанию
    list_search = list()
    searched_list = [['id', 'head', 'body', 'datatime']]

    list_search = notes_parse()
    if oper == 4: #поиск по любому словосочетанию по всей заметке
        for i in list_search[1::]:
            for j in i:
                if str_notes in j:
                    searched_list.append(i)
                    break
    elif oper == 5: #поиск по id
        for i in list_search[1::]:
            if str_notes == i[0]:
                searched_list.append(i)
                break   
    elif oper == 6: # поиск по дате
        for i in list_search[1::]:
            if i[3].find(str_notes) != -1:
                searched_list.append(i)
                break
    if len(searched_list) > 1: return searched_list
    else: return ['ничего не найдено']     

def deleted_notes(id_notes):# удаление записи по id
    list_result = list()
    count = 0
    list_deleted_notes = list()
    list_parse = notes_parse()
    for i in range(0,len(list_parse)):
        if not (str(id_notes) == list_parse[i][0]): #создание нового списка, без удаляемой строки
            list_result.append(list_parse[i])
        else: list_deleted_notes = list_parse[i]
    for i in list_result[1::]: #перезапись id
        i[0] = str(count)
        count += 1
    if len(list_deleted_notes) > 0 and id_notes != 'id':    
        list_write(list_result) #функция перезаписи в файл
        print('Следующая запись удалена:' + str(list_deleted_notes))
    else:
        print('Нет такого id')    

def list_write(list_input): #перезапись файла данными из списка
    for i in range(len(list_input)):
        for j in range(len(list_input[i])):
            list_input[i][j] = list_input[i][j] + ";"
        list_input[i][-1] = list_input[i][-1][:len(list_input[i][j])-1:] + "\n"


    with open ('notes.csv', 'w', encoding='utf-8') as data:
        for i in list_input:
            data.writelines(i)

def edit_notes(id_notes, new_data): #редактирование записи по id
    list_edit = list()
    new_edited = list
    list_data = new_data.split(';')

    list_edit = notes_parse()
    for i in range(1, len(list_edit)):
        if (str(id_notes) == list_edit[i][0]):
            new_edited = list_edit[i]
            for j in range(0, len(list_data)):
                list_edit[i][j+1] = list_data[j]

    if len(list_edit) > 0 and id_notes != 'id':    
        list_write(list_edit) #функция перезаписи в файл
        print('Запись изменена на: ' + str(new_edited))
    else:
        print('Нет такого id') 