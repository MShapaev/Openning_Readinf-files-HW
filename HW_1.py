from pprint import pprint
import requests
import os
#  Я работаю в папке C:\Users\Shapaev\PycharmProjects\Open_Read files\Openning_Readinf-files-HW
#  В эту папку я скопировал папку py-homework-basic-files из учебного git
#  Задача №1:
#  Создаем словарь cook_book из файла recipes.txt
def create_cook_book():
    # Находим файл в папке:
    current = os.path.abspath('py-homework-basic-files')
    folder = '2.4.files'
    file = 'recipes.txt'
    full_path = os.path.join(current, folder, file)
    with open(full_path, 'r', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredient_count = int(file.readline())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient = file.readline().strip()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients.append(
                    {'ingredient_name': ingredient_name,
                     'quantity': quantity,
                     'measure': measure}
                )
            cook_book[dish_name] = ingredients
            file.readline()
        return cook_book

#  Задача №2:
#  функция, которая на вход принимает список блюд dishes из cook_book
#  и количество персон, для кого мы будем готовить
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book()
    shop_list = {}
    #  перебираем блюда в списке dishes:
    for dish_name in dishes:
        for dish in cook_book:
            if dish_name == dish:
                #  Пусть i (ingredient) - словарь с каждым отдельным ингредиентом из cook_book:
                for i in cook_book[dish]:
                    #  Проверка условия, что в итоговом словаре уже есть ингредиент,
                    #  тогда добавляем необходимое количество в ключ 'quantity'. В противном случае - просто создаем его в словаре
                    if i['ingredient_name'] in shop_list:
                        shop_list[i['ingredient_name']]['quantity'] += int(i['quantity']) * person_count
                    else:
                        shop_list[i['ingredient_name']] = {'measure': i['measure'],
                                                           'quantity': int(i['quantity']) * person_count}
    return shop_list


print('cook_book = ')
pprint(create_cook_book(), sort_dicts=False)
print()
print('Список покупок:')
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
print()
#  Задача №3:


#  Забираем файлы в папке C:\Users\Shapaev\PycharmProjects\Open_Read files\Openning_Readinf-files-HW\
#  py-homework-basic-files\2.4.files\sorted. Пишем функцию, которая читает файл и возвращает список строк
def open_file(file_name):
    current = os.path.abspath('py-homework-basic-files')
    folder1 = '2.4.files'
    folder2 = 'sorted'
    full_path = os.path.join(current, folder1, folder2, file_name)

    with open(full_path, encoding='utf-8') as f:
        res = f.readlines()
        return res

#  Функция, которая читает файлы, записанные в рабочем каталоге C:\Users\Shapaev\PycharmProjects\Open_Read files\
#  Openning_Readinf-files-HW:
def open_rev_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        res = f.readlines()
        return res


#  Вспомогательная функция для сортировки списков по длине:
def sort_func(lst):
    return len(lst)


#  Функция записи служебной информации в шапке файла:
def title_func(file_name):
    text = open_file(file_name)
    text.insert(0, str(len(open_file(file_name))) + '\n')
    text.insert(0, file_name + '\n')
    with open(file_name, 'w', encoding='utf-8') as file:
        res = file.writelines(text)
        return f'файл {file_name} перезаписан в директорию {os.getcwd()}'


#  Функция, объединяющая файлы в один в директории C:\Users\Shapaev\PycharmProjects\Open_Read files\
#  Openning_Readinf-files-HW:
def merge_files():
#  Записываем файлы с служебной информацией, а затем объединяем их в один список и сортируем по количеству строк:
    title_func('1.txt')
    title_func('2.txt')
    title_func('3.txt')
    files_list = [open_rev_file('1.txt'), open_rev_file('2.txt'), open_rev_file('3.txt')]
    sorted_len_files = sorted(files_list, key=sort_func)
#  Т.к. на выходе мы должны получить список строк (не вложенный), то добавляем все строки в один список циклом for:
    res = []
    for i in sorted_len_files:
        res.extend(i)
#  Записываем полученный список в файл result.txt
    with open('result.txt', 'w') as f:
        f.writelines(res)
    return f'Файл result.txt записан в директорию {os.getcwd()} записан'

print(merge_files())

