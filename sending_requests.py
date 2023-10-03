import requests
import configuration
import data

#Cоздаю новый заказ
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)
#Сохраняю номер трека заказа
def get_order_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO,
                        params={"t": track_number})

