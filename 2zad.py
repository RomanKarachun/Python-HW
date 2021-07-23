import random
# Кол-во жизней
lives = 10
print ("Попробуйте угадать какого животного мы загадали!")
# Список слов
word_variants = ["собака", "попугай", "енот", "кошка", "кролик", "заяц", "крокодил", "ящерица", "бегемот", "слон",]
# Слово, которое выбрали
word_right = random.choice(word_variants)

# Слово из "_" с угаданными символами
word_in_game = "_" * len(word_right)

while("_" in word_in_game) and (lives > 0):
    print("Осталось жизней: ", lives)
    print(word_in_game)
    letter = input("Введите букву:")
# Проверка, есть ли буква в слове
    if letter in word_right:
        print("Есть такая буква!")
        index = -1
        # Замена символов на игровом поле на правильную букву
        while word_in_game.count(letter) != word_right.count(letter):
            index = word_right.find(letter, index + 1)
            word_in_game = word_in_game[:index] + letter + word_in_game[index + 1:]
    else:
        lives -= 1
        print("К сожалению, такой буквы нет :(")
        print("*" * 10)

if lives > 0:
    print("Было задано слово: ", word_right)
    print("Поздравляю, вы выиграли!")
else:
    print("Было задано слово: ", word_right)
    print("В следующий раз точно повезёт!")
