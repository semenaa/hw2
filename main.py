import os.path

# Задание 1
menu = {}
ROOT_PATH = os.getcwd()
FILE_NAME = 'recipes.txt'
full_path = os.path.join(ROOT_PATH, FILE_NAME)


# Добавить ингредиент в список, сформировать соответствующую структуру данных
def add_ingredients(dish_name, menu, ingr):
    if dish_name in menu.keys():
        menu[dish_name] += [{'ingr_name': ingr[0], 'quantity': int(ingr[1]), 'measure': ingr[2]}]
    else:
        menu[dish_name] = [{'ingr_name': ingr[0], 'quantity': int(ingr[1]), 'measure': ingr[2]}]


with open(full_path, encoding='utf-8') as f:
    dish_name = ''
    ingr_count = 0
    for line in f:
        # Убрать переносы строки
        line = line.strip('\n')
        # Если название блюда еще пустое, заполнить из строки
        if dish_name == '':
            dish_name = line
        else:
            # Если количество ингредиентов еще пустое, заполнить из строки
            if ingr_count == 0:
                ingr_count = int(line)
                counter = 0
            # Далее набить ингредиенты, сверяясь со счетчиком
            else:
                counter += 1
                if counter <= ingr_count:
                    ingr = line.split(sep=' | ')
                    add_ingredients(dish_name, menu, ingr)
                # Если текущая строка пустая, значит, описание блюда закончилось,
                # обнуляем соответствующие переменные для следующего блюда
                elif line == '':
                    dish_name = ''
                    ingr_count = 0
                    # continue
                else:
                    print('Ошибка! Неверно указано количество ингредиентов')

# Задание 2
def get_shop_list_by_menu(dishes, person_count):
    ingrs = {}
    for dish in dishes:
        if dish in menu.keys():
            # Для каждого эл-та списка исходной структуры данных
            for ingr in menu[dish]:
                ingr_name = ingr['ingr_name']
                # если такой элемент уже в нашем словаре есть
                if ingr_name in ingrs.keys():
                    # увеличить имеющееся кол-во с учетом числа персон
                    ingrs[ingr_name]['quantity'] += ingr['quantity'] * person_count
                # В противном случае создать с учетом числа персон
                else:
                    ingrs[ingr_name] = {'measure': ingr['measure'], 'quantity': ingr['quantity'] * person_count}
    return ingrs

print(get_shop_list_by_menu(['Омлет', 'Фахитос'], 5))

