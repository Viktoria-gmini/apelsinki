# Импортируем библиотеку, соответствующую типу нашей базы данных
# В данном случае импортируем все ее содержимое, чтобы при обращении не писать каждый раз имя библиотеки, как мы делали в первой статье
from peewee import *

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
conn = SqliteDatabase('Chinook_Sqlite.sqlite')

# ТУТ БУДЕТ КОД НАШИХ МОДЕЛЕЙ

# Создаем курсор - специальный объект для запросов и получения данных с базы
cursor = conn.cursor()

# ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ

# Не забываем закрыть соединение с базой данных
conn.close()