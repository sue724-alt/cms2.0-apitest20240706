import pymysql
from common.yaml_util import read_config_file, get_object_path


class MysqlrUtil:
    def __init__(self):
        host = read_config_file('mysql','host')
        user = read_config_file('mysql', 'user')
        passwd = read_config_file('mysql', 'passwd')
        database = read_config_file('mysql', 'database')
        charset = read_config_file('mysql', 'charset')

        self.connect = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database,
            charset=charset
        )
        self.cursor = self.connect.cursor()
    def sql(self,sql):
        self.cursor.execute(sql)
        data_list = self.cursor.fetchall()
        return data_list

    def __del__(self):
        self.connect.close()
        self.cursor.close()


if __name__ == '__main__':
    data = MysqlrUtil().sql('SELECT * FROM test01')
    print(data[0][1])