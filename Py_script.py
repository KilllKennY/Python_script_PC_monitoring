import datetime
import psutil
from time import sleep
import requests


def cpu_monitoring() -> None:
    while True:
        ram: float = psutil.virtual_memory().percent
        cpu: float = psutil.cpu_percent(interval=1)
        disk: float = psutil.disk_usage('/').percent
        print(f'CPU:{cpu},  RAM:{ram},  DISK:{disk}')
        if ram >= 90 or cpu >= 90 or disk >= 80:
            requests.post('https://api.github.com/user', auth=('user', 'pass'), data=datetime.datetime, json=f'Alert: CPU:{cpu},  RAM:{ram},  DISK:{disk}')
        sleep(1)


if __name__ == '__main__':
    cpu_monitoring()
