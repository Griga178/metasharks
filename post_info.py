import random
import requests
from get_info import get_colors, get_models

color_list = [
                'Красный',
                'Оранжевый',
                'Желтый',
                'Зеленый',
                'Голубой',
                'Синий',
                'Фиолетовый',
                'Черный',
                'Белый',
                'Серый',
                'Бордовый',
                'Спелая вишня',
                'Рубиновый',
                'Серебряный',
                'Бронзовый'
            ]

brand_model_dict = {
            'KIA': ['k5', 'Rio', 'Soul', 'Seltos'],
            'BMW': ['x1', 'x2', 'x3', 'x4', 'x5', 'x6'],
            'Audi': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'],
            'Ford': ['Transit', 'Mustang', 'Focus', 'Mondeo'],
            'Honda': ['Civic', 'Accord', 'CR-V'],
            'Hyundai': ['Solaris', 'Tucson', 'Sonata'],
            'Wolksvagen': ['Polo', 'Passat', 'Golf', 'Jetta', 'Touran'],
            }

def post_color():
    url = 'http://127.0.0.1:8000/api/color/'
    for color_req in color_list:
        data = {"name": color_req}
        response = requests.post(url, json = data)
        print(response.json())

def post_brand_model():
    brand_url = 'http://127.0.0.1:8000/api/brand/'
    model_url = 'http://127.0.0.1:8000/api/model/'
    for brand_name in brand_model_dict:
        brand_data = {"name": brand_name}
        response = requests.post(brand_url, json = brand_data)
        brand_id = response.json()['id']
        print('Марка:', response.json())

        for model_name in brand_model_dict[brand_name]:
            model_data = {"name": model_name, "brand_name": brand_id}
            response = requests.post(model_url, json = model_data)
            print('Модель:', response.json()["name"])

def post_orders():
    order_url = 'http://127.0.0.1:8000/api/order/'
    color_id_list = [color_d['id'] for color_d in get_colors()]
    model_id_list = [model_id['id'] for model_id in get_models()]
    date_list = ['2022-10-01', '2022-10-02', '2022-10-03', '2022-10-04',
                '2022-10-05', '2022-10-06', '2022-10-07', '2022-10-08',
                '2022-10-09', '2022-10-10', '2022-10-11', '2022-10-12']
    for model_id in model_id_list:
        send_dict = {}
        send_dict['color_name'] = random.choice(color_id_list)
        send_dict['model_name'] = model_id
        send_dict['amount'] = random.randint(1,30)
        appen_date = random.randint(0, 1)
        if appen_date: # не устанавливаем дату - сегодня
            send_dict['order_date'] = random.choice(date_list)
        response = requests.post(order_url, json = send_dict)
        print(response.json())

def model_delete_by_id(list_id):
    for model_id in list_id:
        url = f'http://127.0.0.1:8000/api/model/{model_id}'
        response = requests.delete(url)
        print(response)

# my_list = [el+1 for el in range(30)]
# model_delete_by_id(my_list)


def post_test_data():
    post_color()
    post_brand_model()
    post_orders()

post_test_data()
