from tkinter import Y
import work_directory as wd
import see_directory as sd
import search_directory as sed
import logging as log
import see_directory as seed

def result_opt():
    print('''\nДобро пожаловать в СПРАВОЧНИК, выберите интересующую вас операцию''')
    print('''
1 - Добавить информацию
2 - Посмотреть справочник
3 - Найти в справочнике
4 - Выйти
''')
 
    result = input('Введите номер операции: ')
    if result == 1:
        data1 = wd.get_name()
        data2 = wd.gen_sername()
        data3 = wd.get_phone()
        log.name_logger(data1,data2,data3)
        return data1,data2,data3, log.again()
         
    elif result == 2:
        return seed.see_directory(), seed.again()
        
    
    elif result == 3:
        return sed.serches(), sed.again()
    elif result == 4:
        print("До встречи!")
    else:
        if result != 1 or result != 2 or result != 3 or result != 4:
            print("ОШИБКА: Введите корректное значение!")
            return result_opt()

