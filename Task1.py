# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def result_text():
    result = [i for i in text.split() if delete_text not in i]
    print(f'Исходный текст:{text}\nРезультат: {" ".join(result)}')

text = input("Введите текст:\n")
delete_text = 'абв'
result_text()