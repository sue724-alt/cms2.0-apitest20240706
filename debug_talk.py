import random
import os
import time
import datetime
from common.parameters_util import read_csv_file, read_testcase_file
from common.yaml_util import read_extract_file, read_config_file



class DubugTalk:

    #获取随机数的方法
    def get_random_number(self,min,max):
        return random.randint(int(min),int(max))

    # 获取时间戳
    def get_time_stamp(self):
        now = datetime.datetime.now()
        timestamp = now.timestamp()
        return timestamp
        # print("当前时间：",now)
        # print("时间戳：",timestamp)

    #获取extract.yaml文件中的值
    def get_extract_data(self,node_name):
        return read_extract_file(node_name)

    # 读取基础路径
    def get_base_url(self,node_name):
        return  read_config_file('base',node_name)

    #获取项目路径，单斜杠
    def get_project_path(self):
        path = os.path.abspath(os.getcwd().split('debug_talk.py')[0])
        return path

    # 获取项目路径,双斜杠
    def get_project_path2(self):
        path = os.path.abspath(os.getcwd().split('debug_talk.py')[0])
        path2 = path.replace("\\","\\\\")
        return path2

    def get_int(self,two_name,node_name):
        csv_data = read_csv_file(two_name)
        print('原始：',csv_data)
        print('取值：',csv_data[0][1])
        print('第一个：',csv_data)
        print('参数：',node_name)
        csv_len= len(csv_data)
        for key in range(0,csv_len):
            for value in range(0,len(csv_data[key])):
                # print('第二层：',csv_data[key][value])
                if csv_data[key][value] == node_name:
                    value_data = int(csv_data[key+1][value])
                    return value_data
    # 读取config.
    def get_config(self,one,two):
        return read_config_file(one,two)


if __name__ == '__main__':
    # re = DubugTalk().get_int('data\create_project.csv','type')
    # re1 = read_testcase_file('/testcase/EngineeringManagement/create_project100.yml')
    # print(type(re),re)
    # print(re1)
    DubugTalk().get_project_path2()
