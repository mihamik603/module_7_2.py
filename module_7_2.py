def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):
            start_position = file.tell()  # Получаем текущую позицию в байтах
            file.write(string + '\n')  # Записываем строку с переходом на новую строку
            strings_positions[(index, start_position)] = string  # Сохраняем в словарь

    return strings_positions


# Пример выполняемого кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
