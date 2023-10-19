import requests
import sqlite3
import sys
import logging
from datetime import datetime

def get_position():
    # Запрашиваем id приложения
    app_id = int(input('Введите id приложения: '))
    
    # Получаем инфу о приложении
    try:
        app_info = requests.get(f'https://itunes.apple.com/lookup?id={app_id}').json()['results'][0]
        logging.info(f"SUCCESSFUL: get requests from itunes")
    except Exception as e:
        logging.error(f"ERROR: get requests from itunes")
        logging.critical(e)
        sys.exit(0)
    
    app_name = app_info['trackName']
    app_words = app_name.split()
    
    # Подключаемся к бд
    try:
        conn = sqlite3.connect('itunes.db')
        logging.info(f"SUCCESSFUL: connect to itunes.db")
    except Exception as e:
        logging.error(f"ERROR: connect to itunes.db")
        logging.critical(e)
        sys.exit(0)
    
    c = conn.cursor()
    
    # Создаем таблицу, если ее еще нет
    c.execute('CREATE TABLE IF NOT EXISTS itunes (id INTEGER, word TEXT, pos INTEGER, date TEXT)')
    
    # Получаем текущую дату
    date = datetime.now().strftime('%Y-%m-%d')
    
    # Для каждого слова в названии приложения
    for word in app_words:
        # Получаем список приложений, соответствующих поисковому запросу
        try:
            search_results = requests.get(f'https://itunes.apple.com/search?term={word}&entity=software').json()['results']
            logging.info(f"SUCCESSFUL: get requests from itunes to search word")
        except Exception as e:
            logging.error(f"ERROR: get requests from itunes to search word")
            logging.critical(e)
            sys.exit(0)
        
        # Находим позицию нашего приложения в выдаче
        pos = next((i for i, result in enumerate(search_results) if result['trackId'] == app_id), None)
        
        # Заносим данные в базу
        c.execute('INSERT INTO itunes VALUES (?, ?, ?, ?)', (app_id, word, pos, date))
    
    # Сохраняем изменения и закрываем соединение с бд
    conn.commit()
    conn.close()

# Наша функция
get_position()
