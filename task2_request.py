import requests
from pprint import pprint
from typing import Any


class RequestParams:
    def __init__(self):
        self._ifns = None
        self._oktmo = None

    def get_ifns(self):
        for i in range(2):
            ifns = input('Введите код ИФНС: ')
            if ifns.isdigit() and len(ifns) == 4:
                self._ifns = ifns
                return self._ifns
            else:
                print('Неверный код ИФНС. Код ИФНС должен состоять из 4 цифр')
        if not self._ifns:
            print('Завершение работы по причине: превышено количество попыпот ввода данных.')

    def get_oktmo(self):
        for i in range(2):
            oktmo = input('Введите ОКТМО: ')
            if oktmo.isdigit() and len(oktmo) == 8:
                self._oktmo = oktmo
                return self._oktmo
            else:
                print('Неверный код ОКТМО. Код ОКТМО должен состоять из 8 цифр')
        if not self._oktmo:
            print('Завершение работы по причине: превышено количество попыпот ввода данных.')


def get_fns_info(ifns: str, oktmo: str) -> Any:
    url = 'https://service.nalog.ru/addrno-proc.json'
    payload = {
        'c': 'next',
        'step': 1,
        'npKind': 'fl',
        'ifns': ifns,
        'oktmmf': oktmo
    }
    res = requests.post(url, data=payload)
    if res.status_code == 200:
        return res.json()
    elif res.status_code >= 500:
        return "Ошибка сервера"
    else:
        return "Ошибка, неверные данные или запрос"


if __name__ == '__main__':
    params = RequestParams()
    ifns = params.get_ifns()
    oktmo = params.get_oktmo()
    result = get_fns_info(ifns, oktmo)
    pprint(result)
