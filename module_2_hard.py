number = int(input('Введите число от 3 до 20: '))
result = []
series_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(number-2):
    for j in range(i+1, number-1, 1):
        if number % (series_number[i]+series_number[j]) == 0:
            result.append(series_number[i])
            result.append(series_number[j])
        else:
             continue
print('Пароль для числа: ', *result)
