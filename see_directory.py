import interface as inter
def see_directory():
    with open("info.csv", 'r') as f:
        for line in f:
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

