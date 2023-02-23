board = list(range(1, 10)) #список с значениями

def draw_board(board): # строим игровое поле
    print(" ")
    for i in range(3):
        if i != 2:
            print(" ", board[0 + i * 3], " | ", board[1 + i * 3], " | ", board[2 + i * 3], " ")
            print("-" * 17)
        else:
            print(" ", board[0 + i * 3], " | ", board[1 + i * 3], " | ", board[2 + i * 3], " ")
    print(" ")

def take_input(player_token): #функция ввода занчений игрока
    valid = False
    while not valid:
        player_answer = input("Укажите номер куда поставить " + player_token + "? =")
        try:
            player_answer = int(player_answer)
        except ValueError: #рпроверка на ввод чисел
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9: # проверка на ввод числа от 1 до 9
            if str(board[player_answer - 1]) not in "XO": #если поле не заято значением игрока
                board[player_answer - 1] = player_token #записываем значение игрока в список
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(board): #проверка выеграл ли игрок
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))#задаем победные комбинации
    for each in win_coord: #запуск цикла по каждой комбинции из картежа
        if board[each[0]] == board[each[1]] == board[each[2]]:#берем индекс победного значения, определяем координату и сравниваем записанные значение в них между собой
            return board[each[0]] #Возвраем значение победителя
    return False #иначе переменная остается ложь


def main(board): #основная функция
    counter = 0 #заводим счетчик
    win = False
    while not win:
        draw_board(board) #запуск функции построениям игрового поля
        if counter % 2 == 0: #определение игрока первый, второй (четный, не четный)
            take_input("X") #запуск функции ввода игрока "X" со передачей переменной "X"
        else:
            take_input("O") #запуск функции ввода игрока "0" со передачей переменной "0"
        counter += 1

        tmp = check_win(board) #обьявления переменной запуск функции определения победных комбинаций
        if tmp: #если истина то
            print(tmp, "выиграл!")#вывод значения перемнной сообщение выеграл
            win = True #смена значения на истену
            break #остановка цикла
        if counter == 9: #если колличество ввода значений равно 9
            print("Ничья!") #то ничья
            break #остановка цикла
    draw_board(board) #запуск функции построениям игрового поля

main(board) #вызов основной игровой функции

input("Нажмите Enter для выхода!") #выход из игры