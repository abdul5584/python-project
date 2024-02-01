import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',passwd='',database='amazon')
cursor=con.cursor()
cursor.execute('select * from customer')
rows=cursor.fetchall()
for i in rows:
    print('cusid:',i[0])
    print('cusname:',i[1])
    print('gender:', i[2])
    print('mobnum:', i[3])
    print('email:', i[4])
