purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(input_list: list) -> float:
    sum = 0
    for i in range(len(input_list)):
        cur_sum = input_list[i].get("price") * input_list[i].get("quantity")
        sum += cur_sum
    return sum


def items_by_category(input_list: list) -> dict:
    category = {}
    for i in range(len(input_list)):
        cur_cat = input_list[i].get("category")
        cur_item = input_list[i].get("item")
        if cur_cat not in category:
            category[cur_cat] = [cur_item]
        elif cur_item not in category[cur_cat]:
            category[cur_cat].append(cur_item)
    return category


def expensive_purchases(input_list: list, min_price: float) -> list:
    e_list = []
    for i in range(len(input_list)):
        if input_list[i].get("price") > min_price:
            e_list.append(input_list[i])
    return e_list


def average_price_by_category(input_list: list) -> dict:
    category = {}
    for i in range(len(input_list)):
        cur_cat = input_list[i].get("category")
        cur_price = input_list[i].get("price")
        if cur_cat not in category:
            category[cur_cat] = [cur_price]
        else:
            category[cur_cat].append(cur_price)

    out_dict = {}
    for key, value in category.items():
        avg = 0
        count = 0
        for k in range(len(value)):
            avg += value[k]
            count += 1
        avg = avg / count
        out_dict[key] = avg
    return out_dict


def most_frequent_category(input_list: list) -> str:
    count = {}
    for i in range(len(input_list)):
        cur_cat = input_list[i].get("category")
        if cur_cat not in count:
            count[cur_cat] = 1
        else:
            count[cur_cat] = count[cur_cat] + 1

    most_n = 0
    most_item = ''
    for key, value in count.items():
        if (value > most_n):
            most_n = value
            most_item = key
    return most_item

print(f'Общая выручка: {total_revenue(purchases)}')
print(f'Товары по категориям: {items_by_category(purchases)}')
print(f'Покупки дороже 1.0: {expensive_purchases(purchases, 1.0)}')
print(f'Средняя цена по категориям: {average_price_by_category(purchases)}')
print(f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}')