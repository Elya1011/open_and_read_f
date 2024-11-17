from pprint import pprint
import os



with open('cool_book.txt', encoding='utf8') as f:
    cook_book = dict()
    for i in f:
        dish = i.strip()
        ingredient_count = f.readline()
        ingredient_list = []
        for j in range(int(ingredient_count)):
            recipe = f.readline().strip().split(' | ')
            ingredient_name, quantity, measure = recipe
            ingredient_list.append({'ingredient_name':ingredient_name, 'quantity':quantity, 'measure':measure})
        f.readline()
        cook_book[dish] = ingredient_list
print(cook_book)

def get_shop_list_by_dishes(dishes: list, person_count: int):
    shop_product = {}
    for dish in dishes:
        if dish in cook_book:
            for product in cook_book[dish]:
                if product['ingredient_name'] in shop_product:
                    shop_product[ingredient_name['product']]['quantity'] += int(product['quantity']) * person_count
                else:
                    shop_product[product['ingredient_name']] = {'measure': product['measure'], 'quantity': int(product['quantity']) * person_count}
        else:
            print('Блюда нет в кулинарной книге')
    pprint(shop_product)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


def count(file: str):  # функция, для подсчета кол-ва строк в файле.
    return sum(1 for _ in open(file, 'r', encoding='utf-8'))


def write_file(writing_file: str, path, locate):
    all_files = []
    for i in list(os.listdir(os.path.join(path, locate))):
        if i.endswith('.txt'):
            all_files.append([count(os.path.join(path, locate, i)), os.path.join(path, locate, i), i])
    for file_from_list in sorted(all_files):
        opening_all_files = open(writing_file, 'a')  # Сюда записываем
        opening_all_files.write(f'{file_from_list[2]}\n')  # Название файлы
        opening_all_files.write(f'{file_from_list[0]}\n')  # Кол-во строк.
        # print(file_from_list)
        with open(file_from_list[1], 'r', encoding='utf-8') as file:  # Путь
            counting = 1
            for line in file:
                opening_all_files.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
                counting += 1
        opening_all_files.write(f'\n')
        opening_all_files.close()


writing_file = os.path.abspath('answer.txt')
path = os.getcwd()
locate = os.path.abspath('.')
write_file(writing_file, path, locate)
