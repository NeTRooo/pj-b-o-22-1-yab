import requests
import time
import json

def check_ecampus(url):
    while True:
        response = requests.get(url)
        data = response.json()
        print(data[0]['uuid'])
        time.sleep(600)

if __name__ == '__main__':
    check_ecampus(url='https://api.heylon.ru/api/players')