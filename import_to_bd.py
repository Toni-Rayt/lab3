
# Создал студент 305 группы Филиппов Владимир

import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    host="192.168.122.62",
    database="lab03",
    user="postgres",
    port=5432,
    password='password'
)
cursor = conn.cursor()
"""
# Путь к CSV-файлу
/home/tini/Csv/region.csv
/home/tini/Csv/country.csv
/home/tini/Csv/city.csv
/home/tini/lab03/coastline/output_convert
"""

csv_file_path = "/home/tini/lab03/coastline/output_convert/ne_10m_coastline.csv"

# Открываем CSV-файл
with open(csv_file_path, 'r') as file:
    # Создаем объект csv.reader
    csv_data = csv.reader(file)
    

    # Итерируемся по строкам CSV-файла
    for row in csv_data:
        shape = float(row[0].replace(',', '.'))  
        segment = float(row[1].replace(',', '.'))  
        latitude = float(row[2].replace(',', '.'))  
        longitude = float(row[3].replace(',', '.'))  

        # SQL-запрос для вставки данных
        query = "INSERT INTO data.coastilne (shape, segment, latitude, longitude) " \
                "VALUES (%s, %s, %s, %s)"

    # Выполнение SQL-запроса с передачей параметров
        cursor.execute(query, (shape, segment, latitude, longitude))
# Фиксируем изменения в базе данных
conn.commit()

# Закрываем соединение
cursor.close()
conn.close()