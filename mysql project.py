import mysql.connector
print('connecting to db')
cnx = mysql.connector.connect(user='user', password='pass',
                              host='127.0.0.1',
                              database='database')
print('connected to db')

name = 'qazal'

sex = 'f'

age = 22

cursor = cnx.cursor()
cursor.execute('INSERT INTO people VALUES (\'%s\' , \'%s\', %i )'%(name,sex,age))
cnx.commit()
cnx.close()