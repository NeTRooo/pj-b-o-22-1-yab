import requests
import time
import json

def check_ecampus(url):
    while True:
        response = requests.get(url)
        data = response.json()
        for i in range(0, 10):
            if data[i] is not None:
                print('Пользователь существует')
            else:
                print('Пользователь не существует')
        time.sleep(600)

if __name__ == '__main__':
    check_ecampus(url='https://api.heylon.ru/api/players')