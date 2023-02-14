import operations as op
import view
import check as ch

def button_click():
    view.get_start()
    while (True):
        oper = ch.check_operation()  # считывание и проверка операции
        if ch.check_file() == 1: #проверка на наличие файла
            if oper == 1: # создание заметки
                op.creat_notes(view.get_notes())
            else: 
                print('Cоздайте хотя бы одну заметку!')
        else:
            if oper == 1:
                print('Заметка уже создана, выберите другую операцию!')
                
            elif oper == 2: # добавление записи в заметку
                op.add_notes(view.get_notes())
                
            elif oper == 3: # весь список заметок
                view.print_notes(op.notes_parse())

            elif oper == 4: #поиск по любому словосочетанию по всей заметке
                view.print_notes(op.search_notes(view.get_searched(), oper))

            elif oper == 5: # поиск по id
                view.print_notes(op.search_notes(view.get_id(), oper))

            elif oper == 6: # поиск по дате
                view.print_notes(op.search_notes(view.get_data(), oper))

            elif oper == 7: # редактирование заметки
                op.edit_notes(view.get_id(),view.get_notes())

            elif oper == 8: # удаление заметки по id
                op.deleted_notes(view.get_id())
                
        if oper == 0: # закрытие программы
            print('Программа завершена')
            exit()
        

        
