import requests

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"  # адрес для апи
KEY = "trnsl.1.1.20200424T182553Z.598cd40fa5ebdec9.774bf80d82ef09a452a3e54ec30fa69461fe068e"  # апи ключ


def translate_me(mytext, lang):
    params = {
        "key": KEY,
        "text": mytext,
        "lang": lang  # пользователь вводит либо "ru-en", либо "en-ru"
    }
    response = requests.get(URL, params=params)
    return response.json()
