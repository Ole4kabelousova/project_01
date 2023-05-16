# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:             

import sqlite3

# Создание таблицы

# connection = sqlite3.connect(r'C:\Users\Дом\Documents\Учеба Оля\homeworks-main\homeworks-main\lvl_4\teatchers.db')
# cursor = connection.cursor()
# sqlquery = """CREATE TABLE if not EXISTS Students(
# Student_Id INTEGER NOT NULL,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL PRIMARY KEY
# );"""
# cursor.execute(sqlquery)
# connection.commit()
# connection.close()

# # Заполнение таблицы

# connection = sqlite3.connect(r'C:\Users\Дом\Documents\Учеба Оля\homeworks-main\homeworks-main\lvl_4\teatchers.db')
# cursor = connection.cursor()
# sqlquery = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# (201, 'Иван', 1),
# (202, 'Петр', 2),
# (203, 'Анастасия', 3),
# (204, 'Игорь', 4);"""
# cursor.execute(sqlquery)
# connection.commit()
# connection.close()

# # Получение данных
def get_connection():
  connection = sqlite3.connect(r'C:\Users\Дом\Documents\Учеба Оля\homeworks-main\homeworks-main\lvl_4\teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()


def get_info_Student_and_School(Student_ID):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT Students.Student_ID, Students.Student_Name, Students.School_ID, School.School_Name 
    FROM Students JOIN School ON School.School_ID = Students.School_ID WHERE Student_Id = ?;"""
    cursor.execute(select_query,(Student_ID,))
    records = cursor.fetchall()
    close_connection(connection)
    print('Информация о школе и студенте:')
    for row in records:
      print ("ID студента:", row[0])
      print ("Имя студента:", row[1])
      print ("ID школы:", row[2])
      print ("Название школы:", row[3])
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных: ", error)

get_info_Student_and_School(204)