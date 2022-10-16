import random
import requests
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
                'Рубиновый'
            ]

brand_model_dict = {
            'KIA': ['k5', 'Rio', 'Soul', 'Seltos'],
            'BMW': ['x1', 'x2', 'x3', 'x4', 'x5', 'x6'],
            'Audi': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']},
            'Ford': ['Transit', 'Mustang', 'Focus', 'Mondeo'],
            'Honda': ['Civic', 'Accord', 'CR-V'],
            'Hyundai': ['Solaris', 'Tucson', 'Sonata'],
            'Wolksvagen': ['Polo', 'Passat', 'Golf', 'Jetta', 'Touran'],
            }


# car_amount = random.randint(0,22)
# car_color = random.choice(color_list)

# def post_color():
#     url = 'color'
#
#     for color in color_list:
#         requests
