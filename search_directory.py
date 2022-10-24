import interface as inter

def serches():
    fopen = open('info.csv',mode='r+')

    fread = fopen.readlines()

    x = input("Введите ключевую информацию:  ")

    for line in fread:

        if x in line:

            print(line)
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