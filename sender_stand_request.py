import requests
import configuration


# Функция для создания нового заказа
def post_new_order(body):
    return requests.post(
        url=configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
    )


# Функция для получения заказа по его трек-номеру
def get_order_by_track(track):
    return requests.get(
        url=configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params={"t": track},
    )