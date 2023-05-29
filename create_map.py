
# Создал студент 305 группы Филиппов Владимир

import psycopg2
import matplotlib.pyplot as plt


# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(host='192.168.122.62', port='5432', dbname='lab03', user='postgres', password='password')
cursor = conn.cursor()
# Загрузка данных из таблицы в DataFrame
cursor.execute("SELECT latitude, longitude FROM data.coastilne" )
data = cursor.fetchall()

# Разделение данных на отдельные списки для широты и долготы
latitudes = [row[0] for row in data]
longitudes = [row[1] for row in data]

# Создание графика
plt.figure(figsize=(10, 8))
plt.scatter(longitudes, latitudes, s=1)  # Размер точек можно настроить по необходимости
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Борозна / Coastline Map")

# Вывод карты
plt.show()

# Закрытие соединения с базой данных
cursor.close()
conn.close()