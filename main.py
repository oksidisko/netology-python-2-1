def read_cook_book(filename):

  f = open(filename, 'r')
  while 1 == 1:
    line = f.readline();

    if line == '':
      break

    dish_name = line.strip()
    ingridient_count = int(f.readline().strip())
    ingridients = []

    for i in range(0, ingridient_count):
      ingridients_line = f.readline().strip()
      ingridients_row = ingridients_line.split('|')
      ingridients.append({
        'ingridient_name': ingridients_row[0].strip(),
        'quantity': int(ingridients_row[1].strip()),
        'measure': ingridients_row[2].strip()
      })

    cook_book[dish_name] = ingridients;

cook_book = {}

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

read_cook_book('./data.txt')
create_shop_list()
