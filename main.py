import os.path

dishes = {}
ROOT_PATH = os.getcwd()
FILE_NAME = 'recipes.txt'
full_path = os.path.join(ROOT_PATH, FILE_NAME)

with open(full_path) as f:
    dish_name = ''
    ingr_count = 0
    for line in f:
        if dish_name == '':
            dish_name = line
        else:
            if ingr_count == 0:
                ingr_count = str(line)
            ingr = line.split(sep='|')
            for i in ingr:
                i.strip()
            dishes[dish_name] += [{'ingr_name': ingr[0], 'quantity': ingr[1], 'measure': ingr[2]}]

pass