import pytest
from debug_talk import DubugTalk
import pymysql  # 导入 pymysql 库（MySQL 数据库）
from common.yaml_util import clear_extract_file

@pytest.fixture(scope='session',autouse=True)
def clear_extract():
    clear_extract_file()

@pytest.fixture(scope='function')
def create_mysqldb_fixture():
    print("=============进入数据库创建流程==============")
    host = DubugTalk().get_config('mysql', 'host')
    user = DubugTalk().get_config('mysql', 'user')
    password = DubugTalk().get_config('mysql', 'password')
    database = DubugTalk().get_config('mysql', 'database') + '_data'
    conn = pymysql.connect(host=host, user=user, password=password,
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

@pytest.fixture(scope='function')
def truncate_mysqldb_fixture():
    print("=============清空数据表==============")
    host = DubugTalk().get_config('mysql', 'host')
    user = DubugTalk().get_config('mysql', 'user')
    password = DubugTalk().get_config('mysql', 'password')
    database2 = DubugTalk().get_config('mysql', 'database2')

    conn = pymysql.connect(host=host, user=user, password=password, database=database2)  # 建立 MySQL 连接
    cursor = conn.cursor()
    print("正在清空student数据表...")
    cursor.execute(
        "TRUNCATE TABLE student")
    print("student数据表清空成功")
    conn.close()
