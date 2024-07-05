import pymysql   # 导入 pymysql 库（MySQL 数据库）
from debug_talk import DubugTalk
host = DubugTalk().get_config('mysql', 'host')
user = DubugTalk().get_config('mysql', 'user')
password = DubugTalk().get_config('mysql', 'password')
database = DubugTalk().get_config('mysql','database') + '_data'
conn = pymysql.connect(host=host, user="root", password=123456,
                           database=database)  # 建立 MySQL 连接
cursor = conn.cursor()
result = cursor.execute("SHOW DATABASES LIKE 'TestDB'")
if result > 0:
        print("数据库存在")
else:
        print("数据库不存在，创建testdb数据库...")
        cursor.execute("create database TestDB")
        print("TestDB数据库创建成功")
conn.commit()
conn.close()

    # 重新连接
conn = pymysql.connect(host=host, user=user, password=password, database='TestDB')  # 建立 MySQL 连接
cursor = conn.cursor()
print("创建student数据表...")
cursor.execute(
        "CREATE TABLE IF NOT EXISTS student(id INT AUTO_INCREMENT PRIMARY KEY,time DATETIME,name VARCHAR(20),age INT,money float )")
print("student数据表创建成功")
conn.close()
