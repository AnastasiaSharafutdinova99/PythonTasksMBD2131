# # Задания
#
# ### Задание 1:
#     Все пункты нужно ввыполнить с использованием ТОЛЬКО срезов
#     * Получите подстроку 'string' из строки test_string
#     * Получите подстроку 'Just' из строки test_string
#     * Получите подстроку 'simple' из строки test_string
#     * Получите каждый 5 символ из строки test_string
#     * Получите каждый 3 символ из строки test_string, начиная с конца.

test_string = 'Just a simple string'

#  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 |  10 |   11 |  12 |  13 |  14 |  15 |  16 |  17 |  18 |  19
#  J |  u |  s |  t |    |  a |    |  s |  i |  m |  p  |   l  |  e  |     |  s  |  t  |  r  |  i  |  n  |  g
# -20| -19| -18| -17| -16| -15| -14| -13| -12| -11| -10 |  -9  | -8  |  -7 |  -6 |  -5 |  -4 |  -3 |  -2 |  -1

print("#1 ", test_string[-6:])
print("#1 ", test_string[0:4])
print("#1 ", test_string[7:13])
print("#1 ", test_string[0::5])
print("#1 ", test_string[19:0:-3])
print("")


# ### Задание 2:
#     Написать функцию, которая будет принимать одно значение с логическими типами,
#     а затем ковертировать их в строковые 'True' и 'False' и возвращать эти значения.

def task2(bool):
    if bool == 1:
        print("#2 true")
    else: print("#2 false")
task2(True)


# ### Задание 3:
#     Написать функцию, которая будет принимать одно значение - список.
#     Вычислить разницу между максимальным и минимальным значением и вернуть его.

def max_min_div():
    new_list = input("#3 Введите список чисел: ").split()
    print(new_list)
    res = max(map(int, new_list)) - min(map(int, new_list))
    return res

print("#3 Разница между максимальным и минимальным значением = ", max_min_div())
print("")


# ### Задание 4:
#     Написать функцию, которая будет принимать одно значение - число.
#     Функция должна возвращать список всех четных чисел в диапозоне от 1 до полученного числа.
#     В этом задании нужно использовать list comprehension.

def even_num():
    number = int(input("#4 Введите число больше 0: "))
    num_list = []
    for x in range(number):
        if x % 2 == 0 and x > 1:
            num_list.append(x)
        if x < 0:
            print("Число должно быть положительным")
    return num_list

print("#4 ", even_num())
print("")

# ### Задание 5:
#     Напишите функцию, который имеет два аргумента - x и y.
#     Функция должна выводить координатный угол, в котором находятся координаты (x, y).
#     Точки внутри координатного угла I имеют положительные абсциссы и ординаты.
#     Точки внутри координатного угла II имеют отрицательные абсциссы и положительные ординаты.
#     Точки внутри координатного угла III имеют отрицательные абсциссы и ординаты
#     Точки внутри координатного угла IV имеют положительные абсциссы и отрицательные ординаты.

def coordinate(x, y):
    # x = int(input("#5 Введите координату x: "))
    # y = int(input("#5 Введите координату y: "))
    if x >= 0 and y >= 0: print("#5 Координатный угол I")
    if x < 0 and y >= 0: print("#5 Координатный угол II")
    if x < 0 and y < 0: print("#5 Координатный угол III")
    if x >= 0 and y < 0: print("#5 Координатный угол IV")

coordinate(int(input("#5 Введите координату x: ")), int(input("#5 Введите координату y: ")))
print("")


# ### Задание 6:
#     Напишите функцию, которая принимает одно значение - число.
#     Функция должна возвращать строку - полученное число в двоичном виде

def to01(int):
    int = int(input("#6 Введите число: "))
    a = ''
    initial_int = int
    while int > 0:
        y = int % 2
        int = int // 2
        a = str(y % 2) + a
    print(f'#6 Число {initial_int} в двоичном виде {a}')

to01(int)


# ### Задание 7:
#     Написать функцию, которая будет принимать одно значение - список.
#     Список содержит числа. Все числа, кроме двух, повторяются как минимум два раза.
#     Вернуть список из этих двух неповторяющихся чисел

def numbers_list():
    num_list = input('#7 Введите список чисел: ').split()
    new_num_list = [el for el in num_list if num_list.count(el) == 1]
    print(f'#7 {new_num_list}')

numbers_list()


# ### Задание 8:
#     Напишите функцию, которая принимает два значения - числа num, length (основное число, количество умножений).
#     Функция должна возвращать список перемножений числа num length раз.
#     Пример: test_function(7, 5) ➞ [7, 14, 21, 28, 35]

def multiplication(num, length):
    for i in range(1, length + 1):
        res = num * i
        print(f'#8 {res}')
    return res

multiplication(int(input("#8 Введите основное число: ")), int(input("#8 Введите количество умножений: ")))


# ### Задание 9:
#     Написать функцию, которая будет принимать одно значение - строку.
#     Функция должна возвращать представление полученной строки закодированной азбукой Морзе.
#     Входная строка может содержать буквы как нижнего, так и верхнего регистра.
#     Между всеми словами присутствует пробел.

def morse_code():
    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    initial_str = list(input("#9 Введите строку: ").upper())
    print('#9', end=' ')
    for el in initial_str:
        print(char_to_dots.get(el), end = '')

morse_code()


# ### Задание 10:
#     Написать функцию, которая будет принимать одно значение - список.
#     Функция должна возвращать самое частое значение в списке (встречается > N/2).
#     Пример: test_function(["A", "A", "A", "B", "C", "A"]) ➞ "A"

def frequent_value():
    values = input('#10 Введите список: ').split()
    # most_frequent_value = ''
    for el in values:
        if values.count(el) >= len(values)/2:
            most_frequent_value = el
    print(f'#10 {most_frequent_value}')

frequent_value()


# ### Задание 11:
#     Создайте функцию для выполнения основных арифметических операций,
#     которая применяет сложение, вычитание, умножение и деление к строковому значению
#     (например, "12 + 24" или "23 - 21" или "12 // 12" или "12 * 21").
#
#     Здесь у нас есть 1 число, за которым следует пробел, затем оператор, за которым следует другой пробел, и 2 число.
#     Возвращаемое значение должно быть числом.
#
#     Применение функции eval() не допускается.
#     В случае деления, всякий раз, когда второе число равно "0", возвращайте -1.

def arithmetic_operations():
    equation = input("#11 Введите уравнение: ").split()
    if equation[1] == "+":
        res = int(equation[0]) + int(equation[2])
    if equation[1] == "-":
        res = int(equation[0]) - int(equation[2])
    if equation[1] == "*":
        res = int(equation[0]) * int(equation[2])
    if equation[1] == "/" or equation[1] == "//":
        if equation[2] != "0":
            res = int(equation[0]) // int(equation[2])
        else:
            res = -1
    return res

print('#11', arithmetic_operations())


# ### Задание 12:
#     Напишите функцию, которая принимает список списков и возвращает значение всех символов в нем,
#     где каждый символ добавляет или отнимает что-то от общего балла.
#
#     Значения символов:
#     # = 5
#     О = 3
#     Х = 1
#     ! = -1
#     !! = -3
#     !!! = -5
#
#     Если итоговый результат отрицательный, верните 0
#     (например, 3 #, 3 !!, 2 !!! и X будет (5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) = -3, так что верните 0.

def total_score():
    symbols_value = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
    symbols_list = []
    symbols_value_list = []
    symbols_count_list = []
    result_score = 0
    input_list = list(input('#12 Введите список: ').split(','))
    for el in input_list:
        symbols_list.append(el.split())
    for i in range(len(symbols_list)):
        if symbols_list[i][0] in symbols_value:
            symbols_list[i].append(symbols_list[i][0])
            symbols_list[i][0] = 1
    for i in range(len(symbols_list)):
        symbols_count_list.append(symbols_list[i][0])
        symbols_value_list.append(symbols_list[i][1])
        sym_val = symbols_value.get(symbols_list[i][1])
        result_score += sym_val * int(symbols_list[i][0])
    if result_score < 0:
        print('#12 Итоговый результат: 0')
    else:
        print(f'#12 Итоговый результат: {result_score}')

total_score()


# ### Задание 13:
#     Написать функцию, которая будет принимать одно значение - строку.
#     Функция определяет свободные и занятые участки пляжа.
#     Строка состоит из двух символов 0 - свободный участок, 1 - занятый участок.
#     Из-за недавних ограничений новый человек не может занять место рядом с другим.
#     Должно быть одно свободное место между двумя людьми, отдыхающими на пляже.
#     Функци должна вернуть число - количество новых людей, которые могут воспользоваться местами на пляже.

def beach(beach_area):
    seats = list(map(int, list(beach_area)))
    # print(seats)
    answer = 0
    for i, j in enumerate(seats[1:]):
        if seats[i-1] == seats[i]:
            if seats[i] == seats[i+1]:
                if seats[i] == 0:
                    seats[i] = 2
                    answer += 1
    if seats[len(seats) - 2] == 0 and seats[len(seats) - 1] == 0:
        seats[len(seats) - 1] = 2
    print(f'#13 Количество новых людей, который могут воспользоваться местами на пляже = {answer}')
    print('#13 Доступные для новых людей места отмечены цифрой 2')
    print('#13', seats)
    return answer

beach(input('#13 Введите свободные и занятые участки пляжа: '))

# ### Задание 14:
#     Написать функцию, которая будет принимать одно значение - строку или список.
#     Необходимо зашифровать строку. Первый элемент строки - код буквы в ascii (например 'a' = 97, a 'A' = 65).
#     Следующий элемент - закодированная с помощью таблицы разница между текущим и предыдущим символом, итд.
#     Если подается список - необходимо расшифровать его.
#     Алгоритм такой же - первое число перекодируется в соответствием с таблицей ascii,
#     второй символ - сумма первого и второго числа перекодированная с помощью таблицы ascii.

def ascii_func(initial_string):
    new_string = initial_string.replace(',', '')
    initial_string.split()
    new_string_list = new_string.split()
    if initial_string[0] != '[':
        result_string = [ord(initial_string[0])]
        for i in range(1, len(initial_string)):
            result = ord(initial_string[i]) - ord(initial_string[i - 1])
            result_string.append(result)
        print('#14', result_string)
    if new_string_list[0] == '[':
        new_string_list.remove('[')
        new_string_list.remove(']')
        result_string = ['']
        test = 0
        for i in range(1, len(new_string_list) + 1):
            test += int(new_string_list[i-1])
            result = chr(test)
            result_string.append(result)
        print('#14', ''.join(result_string))

ascii_func(input('#14 Введите строку: '))


# ### Задание 15:
#     Создайте функцию, которая определяет, может ли c каждого места в концертном заде видеть сцену.
#     С места можно увидеть сцену, если значение этого места (указано во входном списке) строго больше,
#     чем значение перед ним.
#     Функция должна возвращать True, если абсолютно все видят сцену, иначе False

def scene_visibility():
    seats = [[1, 2, 3, 2, 1, 1],
             [2, 4, 4, 3, 2, 2],
             [5, 5, 5, 5, 4, 4],
             [6, 6, 7, 6, 5, 5]]

    # seats = [[1, 2, 3, 2, 1, 1],
    #          [2, 4, 4, 3, 2, 2],
    #          [5, 5, 5, 10, 4, 4],
    #          [6, 6, 7, 6, 5, 5]]

    new_seats = list(zip(*seats))
    res_list = []
    for i in range(len(new_seats)):
        for j in range(1, len(new_seats[i])):
            if new_seats[i][j-1] < new_seats[i][j]:
                res_list.append('True')
            elif new_seats[i][j-1] > new_seats[i][j]:
                res_list.append('False')
    if res_list.count('False') > 0:
        return False
    else:
        return True

print('#15', scene_visibility())


# ### Задание 16:
#     Создать функции, которая будет строить лестницу, используя знаки ‘_’ и ‘#’.
#     Положительное значение обозначают, что направление лестницы направленно вверх и вниз для отрицательных значений.
#     Замечания:
#     Возвращаемая строка дополняется символом перехода на новую строку \n

def stair(stair_count):
    res_stair = ''
    if stair_count > 0:
        for count in range(1, stair_count + 1):
            res_stair += '_' * (stair_count - count) + '#' * count + '\n'
    elif stair_count < 0:
        for count in range(stair_count, 0):
            res_stair += '_' * abs(stair_count - count) + '#' * abs(count) + '\n'
    return res_stair

print(stair(int(input('#16 '))))


# ### Задание 17:
#     Имеется строк из символов в нижнем регистре ascii[["a".."z"]].
#     Нужно сократить строку следующим образом: берется пара соседних символов и если они одинаковы, то они удаляются.
#     Например aab должно превратится в b.
#     Нужно удалить как можно больше символов. Если результирующая строка пустая, нужно вернуть "Empty String"

def reduced_string():
    initial_string = list(input('#17 Введите строку: '))
    initial_string_len = len(initial_string)
    for i in range(initial_string_len):
        if i >= initial_string_len:
            break
        if initial_string[i - 1] == initial_string[i]:
            el1 = initial_string[i - 1]
            el2 = initial_string[i]
            initial_string.remove(el1)
            initial_string.remove(el2)
        initial_string_len = len(initial_string)
    if len(initial_string) == 0:
        print('#17 Empty String')
    else:
        print('#17 ', end='')
        print(''.join(initial_string), end='')

reduced_string()


# ### Задание 18:
#     Создать функцию, которая вернет ближайшую к текущей странице главу.
#     Если две главы одинаково близко, то выбирается та, которая находится на большей по порядку странице.

chapter_dict = {'Chapter 1' : 1, 'Chapter 2' : 15, 'Chapter 3' : 37}
# chapter_dict = {'New Beginnings' : 1, 'Strange Developments' : 62, 'The End?' : 194, 'The True Ending' : 460}
# chapter_dict = {'Chapter 1a' : 1, 'Chapter 1b' : 5}

def nearest_chapter(book_chapters, sheet_num):
    chapter_keys_list = list(book_chapters.keys())
    chapter_start_list = list(book_chapters.values())
    for k in range(len(chapter_start_list)):
        if k == len(chapter_start_list) - 1:
            break
        if sheet_num in range(chapter_start_list[k], chapter_start_list[k + 1] + 1):
            if abs(chapter_start_list[k] - sheet_num) > abs(chapter_start_list[k + 1] - sheet_num):
                print('#18', chapter_keys_list[k + 1])
                return
            elif abs(chapter_start_list[k + 1] - sheet_num) > abs(chapter_start_list[k] - sheet_num):
                print('#18', chapter_keys_list[k])
                return
            elif abs(chapter_start_list[k] - sheet_num) == abs(chapter_start_list[k + 1] - sheet_num):
                print('#18', chapter_keys_list[k + 1])
                return

nearest_chapter(chapter_dict, 3)




