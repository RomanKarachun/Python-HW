# Объявляем файлы FIN и FOUT для ввода-вывода данных
FIN  = open('input.txt',  'r')
FOUT = open('output.txt', 'w')

# Считываем весь файл при помощи метода read(),
# результат разбиваем на поля по пробельным символам методом split()
# и записываем в список InputData
InputData = FIN.read().split()
N = int(InputData[0])
M = int(InputData[1])
H = int(InputData[2])
# Теперь в элементах списка InputData[0] и InputData[1]
# записаны два входных числа в виде строк.
# Преобразуем их к типу int и запишем их сумму в переменную Answer
a=H//N
k=0
# Проверяем наши условия
if N >=1 and N<=H and H<=100 and M>=1 and M <=100:
    # Находим необходимый ответ с помощью цикла while
    while M>0:
       M=M-a
       k+=1
    # Выведем результат в файл при помощи метода write
    FOUT.write(str(k) + '\n')
else:
    FOUT.write('Проверьте правильность введённых данных!')
# Закроем файлы FIN и FOUT
FIN.close()
FOUT.close()
