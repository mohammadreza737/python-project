import mysql.connector

cnx = mysql.connector.connect(user='user', password='pass',
                              host='127.0.0.1',
                              database='datatabase')



cursor = cnx.cursor()
query = 'select * from people;'
cursor.execute(query)
for (name,sex,age) in cursor:
    if sex == 'f':
        print('the name of %s her %s and%i'%(name,sex,age))
    else:
       print ('the name of %s is %s and%i'%(name,sex,age))
    
cnx.close()