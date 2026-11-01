<<<<<<< HEAD
import data
import sender_stand_request


# Тест проверяет, что по треку можно получить данные о заказе
def test_get_order_by_track():
    # Создаем заказ и сохраняем ответ
    response_create = sender_stand_request.post_new_order(data.order_body)
    
    # Извлекаем трек-номер из тела ответа
    track = response_create.json()["track"]
    
    # Выполняем запрос на получение заказа по треку
    response_get = sender_stand_request.get_order_by_track(track)
    
    # Проверяем, что код ответа равен 200
    assert response_get.status_code == 200

    # Фролов Константин, 49-я когорта — Финальный проект. Инженер по тестированию плюс
=======
import data
import sender_stand_request


# Тест проверяет, что по треку можно получить данные о заказе
def test_get_order_by_track():
    # Создаем заказ и сохраняем ответ
    response_create = sender_stand_request.post_new_order(data.order_body)
    
    # Извлекаем трек-номер из тела ответа
    track = response_create.json()["track"]
    
    # Выполняем запрос на получение заказа по треку
    response_get = sender_stand_request.get_order_by_track(track)
    
    # Проверяем, что код ответа равен 200
    assert response_get.status_code == 200
>>>>>>> 08e9caedfe9bcdb2b2b4832e31896540a177e4c6
