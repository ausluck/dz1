# 1. Програма буде брати зі списку слів одне рандомне слово.
# 2. Програма буде отримувати від користувача число - кількість спроб вгадати
# 3. Далі програма буде чекати від користувача або букву, або ціле слово.
# 4. Якщо користувач пише слово, програма повинна перевіряти чи це не те саме число, якщо так то говорити що користувач вгадав слово, або писати що слово не правильне.
# 5. Якщо користувач ввів літеру, програма повинна перевірити чи є ця літера у нашому слові, та якщо є, виводити наше слово, де зірочками будуть закриті всі літери, які користувач ще не вгадав, або "Такої літери немає"
# 6. Якщо кількість спроб закінчиться, потрібно сказати користувачю, що він програв та закінчити роботу програми.
#
# Приклад:
# Програмою обрано слово "apple"
# Вхід: 10 (10 спроб вгадати слово)
# Вхід: "a"
# Вихід: "a****"
# Вхід: "d"
# Вихід: "Такої літери немає"
# Вхід: "l"
# Вихід: "a**l*"
# Вхід: "e"
# Вихід: "a**le"
# Вхід: "apple"
# Вихід: "Вітаю, ви вгадали слово"
# Код програми залейте до вашого репозиторію та надішліть посилання у відповідь.


import random

words_list = ["apple", "book", "city", "dance", "elephant", "flower", "garden", "house", "ice", "jump"]

random_word = random.choice(words_list)

#Кількість спроб
attempts = int(input("Enter a number of attempts: "))

#Створюємо масив зірочок для загаданого слова
guessed_word = ["*" for _ in random_word]

#Основний цикл
while attempts > 0:
    guess = input("Enter one letter or a whole word: ")

#Перевірка на одну літеру
    if len(guess) == 1 and guess.isalpha():
        if guess in random_word:
            # Оновлюємо відгадане слово
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    guessed_word[i] = guess  # Замінюємо зірочку на вгадану літеру
            print("Correct! Current word: ", "".join(guessed_word))
        else:
            print("Wrong letter!")
            attempts -= 1  # Зменшуємо кількість спроб
            print(f"Attempts left: {attempts}")

        # Якщо введено ціле слово
    elif len(guess) > 1 and guess.isalpha():
        if guess == random_word:
            print(f"Congratulations! You guessed the word: {random_word}")
            break
        else:
            print("Wrong word!")
            attempts -= 1  # Зменшуємо кількість спроб
            print(f"Attempts left: {attempts}")

        # Перевіряємо, чи вгадане слово повністю
    if "*" not in guessed_word:
        print(f"Congratulations! You've guessed the word: {random_word}")
        break

# Якщо спроби закінчилися
if attempts == 0:
    print(f"Game over! The correct word was: {random_word}")




