from datetime import datetime as dt
import interface as inter

def name_logger(data1,data2,data3):
    time = dt.now().strftime('%H:%M')
    with open('info.csv', 'a') as file:
        file.write('{};name;{};sername;{};phone{}\n'
                    .format(time,data1,data2,data3))
def again():
    print("Вернуться в предыдущее меню? 'Y' - Yes, 'N' - No")

    res = input()
    if res.upper() == 'Y':
        return inter.result_opt()
    elif res.upper() == 'N':
        print("До встречи!")
    else:
        if res.upper() != 'Y' or res.upper() != 'N':
            print("Ошибка ввода") 
            return again()  