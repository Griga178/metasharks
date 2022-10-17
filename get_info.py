import requests

def get_colors(id = ''):
    url = f'http://127.0.0.1:8000/api/color/{id}'
    response = requests.get(url)
    return response.json()

def get_brands(id = ''):
    url = f'http://127.0.0.1:8000/api/brand/{id}'
    response = requests.get(url)
    return response.json()

def get_models(id = ''):
    url = f'http://127.0.0.1:8000/api/model/{id}'
    response = requests.get(url)
    return response.json()

def get_orders(id = ''):
    url = f'http://127.0.0.1:8000/api/order/{id}'
    response = requests.get(url)
    return response.json()

def get_cars_sum_by_color():
    url = 'http://127.0.0.1:8000/api/colors_order/'
    response = requests.get(url)
    return response.json()

def get_cars_sum_by_model():
    url = 'http://127.0.0.1:8000/api/brands_order/'
    response = requests.get(url)
    return response.json()

def all_requests(id = ''):
    print(get_colors(id))
    print(get_brands(id))
    print(get_models(id))
    print(get_orders(id))

    print(get_cars_sum_by_color())
    print(get_cars_sum_by_model())

if __name__ == "__main__":
    # all_requests()
    print(get_brands())
