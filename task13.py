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
        answer += 1
    if seats[0] == 0 and seats[1] == 0:
        seats[0] = 2
        answer += 1
    print(f'#13 Количество новых людей, который могут воспользоваться местами на пляже = {answer}')
    print('#13 Доступные для новых людей места отмечены цифрой 2')
    print('#13', seats)
    return answer

beach(input('#13 Введите свободные и занятые участки пляжа: '))