# Вводим наши значения
N=int(input("Высота частокола по древнерусским ГОСТам (в метрах): "))
M=int(input("Целое количество кольев, необходимое для постройки частокола: "))
H=int(input("Высота древних деревьев острова Буян (в метрах): "))
# Находим целую часть от деления
a=H//N
k=0
# Проверяем наши условия
if N >=1 and N<=H and H<=100 and M>=1 and M <=100:
    # Находим необходимый ответ с помощью цикла while
    while M>0:
       M=M-a
       k+=1
    print("Количество деревьев, которые будут отданы под топор:", k)
else:
    print("Проверьте правильность введённых данных!")
