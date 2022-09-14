"""Tasks 4.4-4.7 from PYTHON-09"""

from collections import Counter, defaultdict
from variables import north, center, south

all_stores = {
    'north': Counter([grocery for check in north for grocery in check]),
    'center':Counter([grocery for check in center for grocery in check]),
    'south': Counter([grocery for check in south for grocery in check])
}

# 4.4 В каком магазине было куплено больше всего товаров.
all_shops_num_sales = {
    shop: sum(number.values()) for shop, number in all_stores.items()
    }
print("The store with the biggest sales is",
      max(all_shops_num_sales, key=all_shops_num_sales.get))

# 4.5 Сколько раз покупали самый редкий товар в магазине north?
# Запишите ответ в числовой форме.
print("Number of sales of the rarest product in the north store is",
      min(all_stores['north'].values()))

# 4.6 Выберите товар, который в магазине center покупали чаще,
# чем в магазине north:
search_product = ['Beer', 'Cola', 'Bread', 'Yoghurt']
for product in search_product:
    if all_stores['center'][product] > all_stores['north'][product]:
        print("The product that was saled in the center "
              "store more often than in the north store is", product)

# 4.7 Есть ли такой товар, который в одном из магазинов покупали чаще,
# чем в двух других вместе взятых?
# Если да, выберите магазин с настолько популярным товаром:
all_products = defaultdict(dict)
for store, products in all_stores.items():
    for product, number in products.items():
        all_products[product][store] = number

for product, stores in all_products.items():
    if max(stores.values()) > (sum(stores.values()) - max(stores.values())):
        print("The product that was bought in one store more often"
              " than in the other two combined is", product, stores)

# 4.8 Определите суммарное число продаж каждого товара во всех магазинах,
# сложив все объекты-счётчики.
# Сколько раз был куплен второй по популярности товар?
# Запишите ответ в числовой форме.
sum_products = Counter()
sum_products = sum(all_stores.values(), sum_products)
print("Most popular products:")
print(sum_products)
