import json
import re
import traceback

import requests
import jsonpath

from common.logger_util import write_log, error_log
from common.yaml_util import read_config_file, read_extract_file, write_extract_file
from common.mysql_util import MysqlrUtil

from debug_talk import DubugTalk

#取消缩进： shift + tab

class RequestUtil():
    session = requests.session()

    def __init__(self,):
        self.base_url =""
        self.last_headers = {}
        self.res_fomat = 0

    # 列表数据解析为非字符串类型
    def list_load(self,data):
        list_data = []
        list_index = 0
        for data_dot in data:
            if isinstance(data_dot, dict):
                # print("=========字典============:",data_dot)
                for key, value in dict(data_dot).items():
                    # print("key:",key,"value:",value)
                    int_value = 0
                    if isinstance(value,str):
                        if 'ddt{{' in value and '}}' in value:
                            new_value = value[5:-2]
                            if new_value.lower() == 'false':
                                int_value = False
                            elif new_value.lower() == 'true':
                                int_value = True
                            elif '.' in new_value:
                                int_value = float(new_value)
                            elif "" == new_value or 'null' == new_value:
                                int_value = None
                            elif '[]' == new_value:
                                int_value = []
                            else:
                                int_value = int(new_value)
                            data[list_index][key] = int_value
                        # 不存在ddt{{}}格式就直接返回
                        else:
                            data[list_index][key] = value
                    elif isinstance(value,dict):
                        self.int_load(value)
                    else:
                        data[list_index][key] = value
            elif isinstance(data_dot, list):
                print("列表内嵌套列表,暂不支持")
                ########暂时没有这种类型，暂不处理#########
            else:
                # =====非字典和列表格式=======
                if 'ddt{{' in data_dot and '}}' in data_dot:
                    new_value = data_dot[5:-2]
                    if new_value.lower() == 'false':
                        int_value = False
                    elif new_value.lower() == 'true':
                        int_value = True
                    elif '.' in new_value:
                        int_value = float(new_value)
                    elif "" == new_value or 'null' == new_value:
                        int_value = None
                    elif '[]' == new_value:
                        int_value = []
                    else:
                        int_value = int(new_value)
                    data[list_index] = int_value
                else:
                    data[list_index] = data_dot
            list_index += 1
        return data

    # 解析为非字符串类型
    def int_load(self,data):
        str_data = json.dumps(data)
        if 'ddt{{' in str_data and '}}' in str_data:
            # data是dict格式
            if isinstance(data, dict):
                for key, value in dict(data).items():
                    int_value = 0
                    # 嵌套列表
                    if isinstance(value, list):
                        list_data = self.list_load(value)
                        data[key] = list_data
                    else:
                        value = str(value)
                        if 'ddt{{' in value and '}}' in value:
                            new_value = value[5:-2]
                            if new_value.lower() == 'false':
                                int_value = False
                            elif new_value.lower() == 'true':
                                int_value = True
                            elif '.' in new_value:
                                int_value = float(new_value)
                            elif "" == new_value or 'null' == new_value:
                                int_value = None
                            elif '[]' == new_value:
                                int_value = []
                            else:
                                int_value = int(new_value)
                            data[key] = int_value
                return data
            # data是list格式
            if isinstance(data, list):
                data = self.list_load(data)
                return data
        # 不存在ddt{{}}格式就直接返回
        else:
            return data
    # 热加载替换解析
    def replace_load(self, data):
        # 不管是什么类型统一转化成字符串格式
        if data and isinstance(data, dict):
            str_data = json.dumps(data)
        elif data and isinstance(data,list):
            str_data = json.dumps(data)
        else:
            str_data = data

        # 替换值
        for i in range(1, str_data.count('${') + 1):
            if '${' in str_data and '}' in str_data:
                start = str_data.index('${')
                end = str_data.index('}', start)
                old_value = str_data[start:end + 1]
                func_name = old_value[2:old_value.index('(')]
                args_value = old_value[old_value.index('(') + 1:old_value.index(')')]
                if len(args_value)==0:
                    new_value = getattr(DubugTalk(), func_name)()
                else:
                    new_value = getattr(DubugTalk(), func_name)(*args_value.split(','))
                str_data = str_data.replace(old_value, str(new_value))

        # 还原数据类型
        # print("===========解析后：",str_data)
        if data and isinstance(data, dict):
            data = json.loads(str_data)
            data = self.int_load(data)
        elif data and isinstance(data,list):
            data = json.loads(str_data)
            data = self.int_load(data)
        else:
            data = str_data

        # 返回
        return data

    # 规范YAML测试用例文件的写法
    def analysis_yaml(self, caseinfo: object) -> object:
        # print("==========caseinfo:",caseinfo)
        try:
            # 1.必须有的四个一级关键字：name,base_url,request,validate
            caseinfo_keys = dict(caseinfo).keys()
            if 'name' in caseinfo_keys and 'base_url' in caseinfo_keys and 'request' in caseinfo_keys and 'validate' in caseinfo_keys:
                # 2.在request一级关键字下必须包括两个二级关键字：method，url
                request_keys = dict(caseinfo['request']).keys()
                if 'method' in request_keys and 'url' in request_keys:
                    # 参数(param,data,json)，请求头，文件上传这些都不能约束
                    self.base_url = caseinfo['base_url']
                    name = caseinfo['name']
                    method = caseinfo['request'].pop('method')
                    # url = caseinfo['request']['url']
                    url = caseinfo['request'].pop('url')
                    headers = None
                    if jsonpath.jsonpath(caseinfo, '$..headers'):
                        headers = caseinfo['request']['headers']
                        del caseinfo['request']['headers']

                    files = None
                    if jsonpath.jsonpath(caseinfo, '$..files'):
                        files = caseinfo['request']['files']
                        for key,value in dict(files).items():
                            files_value = self.replace_load(value)
                            files[key] = open(files_value,'rb')
                        del caseinfo['request']['files']
                    res = self.send_request(name =name,method=method,
                                            url=url,
                                            headers=headers, files=files,
                                            **caseinfo['request'])

# '----------------------------------------------------------------------------'
                    status_code = res.status_code
                    try:
                        return_data = res.json()  # json提取
                        return_text = json.dumps(return_data)
                    except:
                        self.res_fomat = 1

                    # 接口关联的变量,既支持正则表达式，也支持json提取
                    if self.res_fomat == 0:
                        return_data = res.json()  # json提取
                        return_text = json.dumps(return_data)
                        if 'extract' in caseinfo:
                            for key, value in dict(caseinfo['extract']).items():
                                # 正则表达式
                                if '(.+?)' in value or '(.*?)' in value:
                                    ze_value = re.findall(value, return_text)
                                    if ze_value:
                                        extract_data = {key: ze_value[1]}
                                        write_extract_file(extract_data)

                                elif value == "content":
                                    if isinstance(return_data,list):
                                        extract_data = {key: return_data[0]}
                                        write_extract_file(extract_data)
                                    elif isinstance(return_data,dict):
                                        extract_data = {key: return_data}
                                        write_extract_file(extract_data)
                                    else:
                                        extract_data = {key: return_data}
                                        write_extract_file(extract_data)
                                # json、list提取
                                else:
                                    if isinstance(return_data, list):
                                        value_data = str(value).split('.')
                                        key_data = value_data[0]
                                        value_data = int(value_data[1])
                                        extract_data = {key: return_data[value_data][key_data]}
                                        write_extract_file(extract_data)
                                    elif isinstance(return_data, dict):
                                        if "."  in str(value):
                                            # 仅针对key加索引类型,如：originalId.0
                                            key_list = str(value).split('.')
                                            value1 = key_list[0]
                                            value2 = int(key_list[1])
                                            value_list = jsonpath.jsonpath(return_data, '$..%s' % value1)
                                            extract_data = {key: value_list[value2]}
                                            write_extract_file(extract_data)
                                        else:
                                            value_data = jsonpath.jsonpath(return_data, '$..%s' % value)
                                            # print("++++++++++++:",value_data)
                                            extract_data = {key: value_data[0]}
                                            write_extract_file(extract_data)


                        # 断言封装
                        yq_result = caseinfo['validate']
                        # print("实际结果：",return_data)
                        self.validate_result(yq_result, return_data, status_code)
                    else:
                        return_text = res.text  # 正则提取
                        if 'extract' in caseinfo:
                            for key, value in dict(caseinfo['extract']).items():
                                # 正则表达式
                                if '(.+?)' in value or '(.*?)' in value:
                                    ze_value = re.findall(value, return_text)
                                    if ze_value:
                                        extract_data = {key: ze_value[1]}
                                        write_extract_file(extract_data)
                                elif value == "content":
                                    extract_data = {key: return_text}
                                    write_extract_file(extract_data)

                        # 断言封装
                        yq_result = caseinfo['validate']
                        self.validate_result(yq_result, return_text, status_code)

                else:

                    error_log('2.在request一级关键字下必须包括两个二级关键字：method，url')
            else:
                error_log("1.必须有的四个一级关键字：name,base_url,request,validate")
        except Exception as f:
            error_log("分析YAML文件异常：异常信息: %s" % str(traceback.format_exc()))

    # # 统一替换方法，data可以是url（string），也可以是参数（字典，字典中包含有列表），也可以是有请求头（字典）
    # def replace_value(self, data):
    #     # 不管是什么类型统一转化成字符串格式
    #     if data and isinstance(data, dict):  # 如果data不为空并且data的类型是一个字典
    #         str_data = json.dumps(data)
    #     else:
    #         str_data = data
    #
    #     # 替换值
    #     for i in range(1, str_data.count('{{') + 1):
    #         if '{{' in str_data and '}}' in str_data:
    #             start = str_data.index('{{')
    #             end = str_data.index('}}', start)
    #             old_value = str_data[start:end + 2]
    #             new_value = read_extract_file(old_value[2:-2])
    #             str_data = str_data.replace(old_value, new_value)
    #
    #     # 还原数据类型
    #     if data and isinstance(data, dict):
    #         data = json.loads(str_data)
    #     else:
    #         data = str_data
    #
    #     # 返回
    #     return data



    # 统一发送请求的方法
    def send_request(self, name, method, url, headers=None,file=None,**kwargs):
        try:
            # 处理method
            self.last_method = str(method).lower()
            # 处理基础路径
            self.base_url = self.replace_load(self.base_url) + self.replace_load(url)
            # 处理请求头
            if headers and isinstance(headers, dict):
                self.last_headers = self.replace_load(headers)
            # 处理请求数据，可能是params，data，json
            for key, value in kwargs.items():
                if key in ['params', 'data', 'json']:
                    kwargs[key] = self.replace_load(value)

            # 收集日志
            write_log("\n-------------接口请求开始-----------")
            write_log("接口名称：%s"%name)
            write_log("接口方式：%s"%self.last_method)
            write_log("接口路径：%s"%self.base_url)
            write_log("请求头：%s"%self.last_headers)
            if 'params' in kwargs.keys():
                write_log("请求参数：%s"%kwargs['params'])
            elif 'data' in kwargs.keys():
                write_log("请求参数：%s"%kwargs['data'])
            elif 'json' in kwargs.keys():
                write_log("请求参数：%s"%kwargs['json'])
            write_log("文件上传：%s"%file)
            # 发送请求s
            res = RequestUtil.session.request(method=self.last_method, url=self.base_url, headers=self.last_headers, **kwargs)
            return res
        except Exception as f:
            error_log("发送请求异常：异常信息: %s" % str(traceback.format_exc()))

    #断言封装
    def validate_result(self,yq_result,sj_result,status_code):
        try:
            """
            :param yq_result: 预期结果
            :param sj_result: 实际结果
            :param status_code: 实际返回的状态码
            :return:
            """
            #解析
            yq_result = self.replace_load(yq_result)

            yq_result_list = []
            #断言是否成功的标记：0是成功，其他失败
            # print('预期结果：',yq_result)
            # print('实际结果：',sj_result,status_code)
            flag = 0
            #解析
            if yq_result and isinstance(yq_result,list):
                # print("预期结果：",yq_result)
                for yq in yq_result:
                    #断言参数解析
                    yq = self.replace_load(yq)
                    for key,value in dict(yq).items():
                        #等于断言
                        if key=='equals':
                            for assert_key,assert_value in dict(value).items():
                                # print("assert_key:",assert_key,"assert_value:",assert_value)
                                if assert_key=="status_code":
                                    if status_code!=assert_value:
                                        flag = flag + 1
                                        error_log("断言失败:"+assert_key+"不等于"+str(assert_value))
                                elif assert_key == "content":
                                    if sj_result != assert_value:
                                        flag = flag + 1
                                        error_log("断言失败:" + assert_key + "不等于" + str(assert_value))
                                else:
                                    #根据key提取所有value
                                    value_list = jsonpath.jsonpath(sj_result,'$..%s'%assert_key)
                                    # print("实际结果key_list:",value_list)
                                    # print("预期结果assert_value:", assert_value)
                                    if value_list:
                                        if assert_value not in value_list:
                                            flag + flag+1
                                            error_log("断言失败:" + assert_key + "不等于" + str(assert_value))
                                    else:
                                        flag = flag+1
                                        error_log("断言失败：返回结果中不存在："+assert_key)
                        #包含断言
                        elif key=="contains":
                            if isinstance(value,str):
                                if value not in sj_result:
                                    flag = flag + 1
                                    error_log("断言失败：返回结果不包含字符串：" + value)
                            else:
                                if value not in json.dumps(sj_result):
                                    flag = flag + 1
                                    error_log("断言失败：返回结果不包含字符串：" + value)
                        #数据库断言
                        elif key == "mysql":
                            for assert_key, assert_value in dict(value).items():
                                if assert_key=="gt":
                                    data = MysqlrUtil().sql(assert_value)
                                    if len(data)==0:
                                        flag = flag + 1
                                        error_log("断言失败:"+assert_key+"不等于"+str(assert_value))

                        #数值大于
                        elif key == "greater_than":
                            for assert_key, assert_value in dict(value).items():
                                key_list = jsonpath.jsonpath(sj_result, '$..%s' % assert_key)
                                # print("key_list:",key_list)
                                # print("实际结果key_list:",key_list,type(key_list[0]))
                                # print("预期结果assert_value:", assert_value,type(assert_value))
                                #取列表中第一条数据进行判断
                                if key_list:
                                    if assert_value > key_list[0]:
                                        flag + flag + 1
                                        error_log("断言失败:" + assert_key + "不大于" + str(assert_value))
                                else:
                                    flag = flag + 1
                                    error_log("断言失败：返回结果中不存在：" + assert_key)
                        # 字符串长度大于
                        elif key == "length_greater_than":
                            for assert_key, assert_value in dict(value).items():
                                key_list = jsonpath.jsonpath(sj_result, '$..%s' % assert_key)
                                # print("key_list:",key_list)
                                # print("实际结果key_list:",key_list,type(key_list[0]))
                                # print("预期结果assert_value:", assert_value,type(assert_value))
                                #取列表中第一条数据进行判断
                                if key_list:
                                    if assert_value > len(key_list[0]):
                                        flag + flag + 1
                                        error_log("断言失败:" + assert_key + "不大于" + str(assert_value))
                                else:
                                    flag = flag + 1
                                    error_log("断言失败：返回结果中不存在：" + assert_key)
                        else:
                            error_log("框架不支持该断言方式")
                    yq_result_list.append(yq)
            # 收集日志
            write_log('预期结果：%s' % yq_result_list)
            write_log('实际结果：%s' % sj_result)
            assert flag==0
            write_log("接口请求成功！")
            write_log("\n-------------接口请求结束-----------\n")

        except Exception as f:
            write_log('实际结果：%s' % sj_result)
            write_log("接口请求失败！")
            write_log("-------------接口请求结束-----------\n")
            error_log("断言异常：异常信息: %s" % str(traceback.format_exc()))

if __name__ == '__main__':
    list_data2 = {'realTime': 'ddt{{false}}', 'triggers': [
        {'effectiveDateTime': 'ddt{{false}}', 'frequencyValue': 'ddt{{1}}', 'freq': 'ddt{{77.77}}', 'freqstr': '',
         'condition': 'A1==100'}]}
    dict_data = {'effectiveDateTime': 'ddt{{false}}', 'frequencyValue': 'ddt{{1}}', 'freq': 'ddt{{77.77}}',
                 'freqstr': '', 'condition': 'A1==100'}
    list_data = [
        {'effectiveDateTime': 'ddt{{false}}', 'frequencyValue': 'ddt{{1}}', 'freq': 'ddt{{77.77}}', 'freqstr': '',
         'condition': 'A1==100'},
        {'effectiveDateTime': 'ddt{{false}}', 'frequencyValue': 'ddt{{1}}', 'freq': 'ddt{{77.77}}', 'freqstr': '',
         'condition': 'A1==100'}]
    dict_data2 = {'effectiveDateTime': False, 'frequencyValue': 1, 'freq': 77.77, 'freqstr': '', 'condition': 'A1==100'}
    list_data3 = ['ddt{{false}}', 'ddt{{77.77}}', 'freqstr']
    dict_data3 = {'realTime': False, 'triggers': [{'effectiveDateTime': '', 'frequencyValue': 'ddt{{1}}', 'frequencyUnit': 2, 'matchAll': False, 'condition': 'A1==100', 'conditionDetail': 1, 'frequencyCheck': False, 'triggerType': 2}]}
    dict_data4 = {'realTime': 'ddt{{$csv{realTime}}}', 'triggers': [{'effectiveDateTime': '2023-05-22T06:15:31.000Z', 'frequencyValue': 'ddt{{1}}', 'frequencyUnit': 'ddt{{1}}', 'matchAll': 'ddt{{false}}', 'condition': '', 'conditionDetail': 'ddt{{1}}', 'frequencyCheck': 'ddt{{false}}', 'triggerType': 'ddt{{1}}'}]}
    list_data5 = [{'archiveSetting': None, 'groupId': 51, 'name': '', 'description': '校验变量名为空', 'typeName': '有符号8位整型', 'config': {'readWriteMode': 0, 'address': '400001', 'interval': 'ddt{{10000}}'}, 'stringLength': 'null', 'zoom': 1, 'digit': None, 'readWriteRule': 1, 'index': 1}]
    shijijieguo = [{'_id': 3, '记录时间': '2023-10-09 14:49:48', '__$按年分组_year': '2023-01-01 00:00:00', '__$按年分组_month': '2023-01-01 00:00:00', '__$按年分组_day': '2023-01-01 00:00:00', '__$按年分组_hour': '2023-01-01 00:00:00', '__$按年分组_minute': '2023-01-01 00:00:00', '__$按年分组_quarter': '2023-01-01 00:00:00', '__$按年分组_week': '2022-12-26 00:00:00', '__$按季度分组_year': '2023-01-01 00:00:00', '__$按季度分组_month': '2023-10-01 00:00:00', '__$按季度分组_day': '2023-10-01 00:00:00', '__$按季度分组_hour': '2023-10-01 00:00:00', '__$按季度分组_minute': '2023-10-01 00:00:00', '__$按季度分组_quarter': '2023-10-01 00:00:00', '__$按季度分组_week': '2023-09-25 00:00:00', '__$按月分组_year': '2023-01-01 00:00:00', '__$按月分组_month': '2023-10-01 00:00:00', '__$按月分组_day': '2023-10-01 00:00:00', '__$按月分组_hour': '2023-10-01 00:00:00', '__$按月分组_minute': '2023-10-01 00:00:00', '__$按月分组_quarter': '2023-10-01 00:00:00', '__$按月分组_week': '2023-09-25 00:00:00', '__$按周分组_year': '2023-01-01 00:00:00', '__$按周分组_month': '2023-10-01 00:00:00', '__$按周分组_day': '2023-10-09 00:00:00', '__$按周分组_hour': '2023-10-09 00:00:00', '__$按周分组_minute': '2023-10-09 00:00:00', '__$按周分组_quarter': '2023-10-01 00:00:00', '__$按周分组_week': '2023-10-09 00:00:00', '__$按日分组_year': '2023-01-01 00:00:00', '__$按日分组_month': '2023-10-01 00:00:00', '__$按日分组_day': '2023-10-09 00:00:00', '__$按日分组_hour': '2023-10-09 00:00:00', '__$按日分组_minute': '2023-10-09 00:00:00', '__$按日分组_quarter': '2023-10-01 00:00:00', '__$按日分组_week': '2023-10-09 00:00:00', '__$按小时分组_year': '2023-01-01 00:00:00', '__$按小时分组_month': '2023-10-01 00:00:00', '__$按小时分组_day': '2023-10-09 00:00:00', '__$按小时分组_hour': '2023-10-09 14:00:00', '__$按小时分组_minute': '2023-10-09 14:00:00', '__$按小时分组_quarter': '2023-10-01 00:00:00', '__$按小时分组_week': '2023-10-09 00:00:00', '__$按分钟分组_year': '2023-01-01 00:00:00', '__$按分钟分组_month': '2023-10-01 00:00:00', '__$按分钟分组_day': '2023-10-09 00:00:00', '__$按分钟分组_hour': '2023-10-09 14:00:00', '__$按分钟分组_minute': '2023-10-09 14:49:00', '__$按分钟分组_quarter': '2023-10-01 00:00:00', '__$按分钟分组_week': '2023-10-09 00:00:00', '__$系统时间_year': '2023-01-01 00:00:00', '__$系统时间_month': '2023-10-01 00:00:00', '__$系统时间_day': '2023-10-09 00:00:00', '__$系统时间_hour': '2023-10-09 14:00:00', '__$系统时间_minute': '2023-10-09 14:49:00', '__$系统时间_quarter': '2023-10-01 00:00:00', '__$系统时间_week': '2023-10-09 00:00:00', '__$DATE1_year': '2023-01-01 00:00:00', '__$DATE1_month': '2023-06-01 00:00:00', '__$DATE1_day': '2023-06-19 00:00:00', '__$DATE1_hour': '2023-06-19 00:00:00', '__$DATE1_minute': '2023-06-19 00:00:00', '__$DATE1_quarter': '2023-04-01 00:00:00', '__$DATE1_week': '2023-06-19 00:00:00', '__$TODAY1_year': '2023-01-01 00:00:00', '__$TODAY1_month': '2023-10-01 00:00:00', '__$TODAY1_day': '2023-10-09 00:00:00', '__$TODAY1_hour': '2023-10-09 00:00:00', '__$TODAY1_minute': '2023-10-09 00:00:00', '__$TODAY1_quarter': '2023-10-01 00:00:00', '__$TODAY1_week': '2023-10-09 00:00:00', '按年分组': '2023', '按季度分组': '2023-04', '按月分组': '2023-10', '按周分组': '2023-42', '按日分组': '2023-10-09', '按小时分组': '2023-10-09 14', '按分钟分组': '2023-10-09 14:49', 'A1': 528.0, 'B1': 3717.888, 'G1': 48.0, 'ROUND1': 3717.9, 'ROUNDUP1': 3717.9, 'ROUNDDOWN1': 3717.8, 'SUM1': 4245.888, 'AVERAGE1': 2122.944, 'COUNT1': 2.0, 'COUNTA1': 2.0, 'MAX1': 3717.888, 'MEDIAN1': 2122.944, 'MIN1': 528.0, 'ABS1': 3717.888, 'max_B1': 3717.888, 'min_B1': 3717.888, '系统时间': '2023-10-09 14:49:47', 'DATE1': '2023-06-19 00:00:00', 'DATEDIF1': '1', 'DAY1': '9', 'DAYS1': '18', 'HOUR1': '14', 'MINUTE1': '49', 'MONTH1': '10', 'NOW1': '2023-10-09 14:49:48', 'SECOND1': '47', 'YEAR1': '2023', 'TODAY1': '2023-10-09 00:00:00', '差值年': 3.0, '差值月': 5.0, '差值天': 26.0, '差值时': 9.0, '差值分': 15.0, '差值秒': 20.0, 'H1': 'Abcf', 'CHAR1': '\\', 'CONCATENATE1': 'Abcf123', 'LEFT2': 'Ab', 'LEN1': '4', 'LOWER1': 'abcf', 'MID12': 'Ab', 'REPLACE1': '替换cf', 'RIGHT1': 'cf', 'TODATE1': '2023-06-19 00:00:00', 'TRIM1': 'Abcf', 'UPPER1': 'ABCF', '去空格后长度': '4', 'AND1': '0', 'FALSE1': '0', 'TRUE1': '1', 'IF1': '及格', 'NOT_true1': '0', 'NOT_false1': '1', 'OR1': '0'}, {'_id': 2, '记录时间': '2023-10-09 14:49:48', '__$按年分组_year': '2023-01-01 00:00:00', '__$按年分组_month': '2023-01-01 00:00:00', '__$按年分组_day': '2023-01-01 00:00:00', '__$按年分组_hour': '2023-01-01 00:00:00', '__$按年分组_minute': '2023-01-01 00:00:00', '__$按年分组_quarter': '2023-01-01 00:00:00', '__$按年分组_week': '2022-12-26 00:00:00', '__$按季度分组_year': '2023-01-01 00:00:00', '__$按季度分组_month': '2023-10-01 00:00:00', '__$按季度分组_day': '2023-10-01 00:00:00', '__$按季度分组_hour': '2023-10-01 00:00:00', '__$按季度分组_minute': '2023-10-01 00:00:00', '__$按季度分组_quarter': '2023-10-01 00:00:00', '__$按季度分组_week': '2023-09-25 00:00:00', '__$按月分组_year': '2023-01-01 00:00:00', '__$按月分组_month': '2023-10-01 00:00:00', '__$按月分组_day': '2023-10-01 00:00:00', '__$按月分组_hour': '2023-10-01 00:00:00', '__$按月分组_minute': '2023-10-01 00:00:00', '__$按月分组_quarter': '2023-10-01 00:00:00', '__$按月分组_week': '2023-09-25 00:00:00', '__$按周分组_year': '2023-01-01 00:00:00', '__$按周分组_month': '2023-10-01 00:00:00', '__$按周分组_day': '2023-10-09 00:00:00', '__$按周分组_hour': '2023-10-09 00:00:00', '__$按周分组_minute': '2023-10-09 00:00:00', '__$按周分组_quarter': '2023-10-01 00:00:00', '__$按周分组_week': '2023-10-09 00:00:00', '__$按日分组_year': '2023-01-01 00:00:00', '__$按日分组_month': '2023-10-01 00:00:00', '__$按日分组_day': '2023-10-09 00:00:00', '__$按日分组_hour': '2023-10-09 00:00:00', '__$按日分组_minute': '2023-10-09 00:00:00', '__$按日分组_quarter': '2023-10-01 00:00:00', '__$按日分组_week': '2023-10-09 00:00:00', '__$按小时分组_year': '2023-01-01 00:00:00', '__$按小时分组_month': '2023-10-01 00:00:00', '__$按小时分组_day': '2023-10-09 00:00:00', '__$按小时分组_hour': '2023-10-09 14:00:00', '__$按小时分组_minute': '2023-10-09 14:00:00', '__$按小时分组_quarter': '2023-10-01 00:00:00', '__$按小时分组_week': '2023-10-09 00:00:00', '__$按分钟分组_year': '2023-01-01 00:00:00', '__$按分钟分组_month': '2023-10-01 00:00:00', '__$按分钟分组_day': '2023-10-09 00:00:00', '__$按分钟分组_hour': '2023-10-09 14:00:00', '__$按分钟分组_minute': '2023-10-09 14:48:00', '__$按分钟分组_quarter': '2023-10-01 00:00:00', '__$按分钟分组_week': '2023-10-09 00:00:00', '__$系统时间_year': '2023-01-01 00:00:00', '__$系统时间_month': '2023-10-01 00:00:00', '__$系统时间_day': '2023-10-09 00:00:00', '__$系统时间_hour': '2023-10-09 14:00:00', '__$系统时间_minute': '2023-10-09 14:48:00', '__$系统时间_quarter': '2023-10-01 00:00:00', '__$系统时间_week': '2023-10-09 00:00:00', '__$DATE1_year': '2023-01-01 00:00:00', '__$DATE1_month': '2023-06-01 00:00:00', '__$DATE1_day': '2023-06-19 00:00:00', '__$DATE1_hour': '2023-06-19 00:00:00', '__$DATE1_minute': '2023-06-19 00:00:00', '__$DATE1_quarter': '2023-04-01 00:00:00', '__$DATE1_week': '2023-06-19 00:00:00', '__$TODAY1_year': '2023-01-01 00:00:00', '__$TODAY1_month': '2023-10-01 00:00:00', '__$TODAY1_day': '2023-10-09 00:00:00', '__$TODAY1_hour': '2023-10-09 00:00:00', '__$TODAY1_minute': '2023-10-09 00:00:00', '__$TODAY1_quarter': '2023-10-01 00:00:00', '__$TODAY1_week': '2023-10-09 00:00:00', '按年分组': '2023', '按季度分组': '2023-04', '按月分组': '2023-10', '按周分组': '2023-42', '按日分组': '2023-10-09', '按小时分组': '2023-10-09 14', '按分钟分组': '2023-10-09 14:48', 'A1': 660.0, 'B1': 4647.36, 'G1': 60.0, 'ROUND1': 4647.4, 'ROUNDUP1': 4647.4, 'ROUNDDOWN1': 4647.3, 'SUM1': 5307.36, 'AVERAGE1': 2653.68, 'COUNT1': 2.0, 'COUNTA1': 2.0, 'MAX1': 4647.36, 'MEDIAN1': 2653.68, 'MIN1': 660.0, 'ABS1': 4647.36, 'max_B1': 4647.36, 'min_B1': 4647.36, '系统时间': '2023-10-09 14:48:59', 'DATE1': '2023-06-19 00:00:00', 'DATEDIF1': '1', 'DAY1': '9', 'DAYS1': '18', 'HOUR1': '14', 'MINUTE1': '48', 'MONTH1': '10', 'NOW1': '2023-10-09 14:49:48', 'SECOND1': '59', 'YEAR1': '2023', 'TODAY1': '2023-10-09 00:00:00', '差值年': 3.0, '差值月': 5.0, '差值天': 26.0, '差值时': 9.0, '差值分': 15.0, '差值秒': 20.0, 'H1': 'Abcf', 'CHAR1': '\\', 'CONCATENATE1': 'Abcf123', 'LEFT2': 'Ab', 'LEN1': '4', 'LOWER1': 'abcf', 'MID12': 'Ab', 'REPLACE1': '替换cf', 'RIGHT1': 'cf', 'TODATE1': '2023-06-19 00:00:00', 'TRIM1': 'Abcf', 'UPPER1': 'ABCF', '去空格后长度': '4', 'AND1': '0', 'FALSE1': '0', 'TRUE1': '1', 'IF1': '及格', 'NOT_true1': '0', 'NOT_false1': '1', 'OR1': '0'}, {'_id': 1, '记录时间': '2023-10-09 14:48:48', '__$按年分组_year': '2023-01-01 00:00:00', '__$按年分组_month': '2023-01-01 00:00:00', '__$按年分组_day': '2023-01-01 00:00:00', '__$按年分组_hour': '2023-01-01 00:00:00', '__$按年分组_minute': '2023-01-01 00:00:00', '__$按年分组_quarter': '2023-01-01 00:00:00', '__$按年分组_week': '2022-12-26 00:00:00', '__$按季度分组_year': '2023-01-01 00:00:00', '__$按季度分组_month': '2023-10-01 00:00:00', '__$按季度分组_day': '2023-10-01 00:00:00', '__$按季度分组_hour': '2023-10-01 00:00:00', '__$按季度分组_minute': '2023-10-01 00:00:00', '__$按季度分组_quarter': '2023-10-01 00:00:00', '__$按季度分组_week': '2023-09-25 00:00:00', '__$按月分组_year': '2023-01-01 00:00:00', '__$按月分组_month': '2023-10-01 00:00:00', '__$按月分组_day': '2023-10-01 00:00:00', '__$按月分组_hour': '2023-10-01 00:00:00', '__$按月分组_minute': '2023-10-01 00:00:00', '__$按月分组_quarter': '2023-10-01 00:00:00', '__$按月分组_week': '2023-09-25 00:00:00', '__$按周分组_year': '2023-01-01 00:00:00', '__$按周分组_month': '2023-10-01 00:00:00', '__$按周分组_day': '2023-10-09 00:00:00', '__$按周分组_hour': '2023-10-09 00:00:00', '__$按周分组_minute': '2023-10-09 00:00:00', '__$按周分组_quarter': '2023-10-01 00:00:00', '__$按周分组_week': '2023-10-09 00:00:00', '__$按日分组_year': '2023-01-01 00:00:00', '__$按日分组_month': '2023-10-01 00:00:00', '__$按日分组_day': '2023-10-09 00:00:00', '__$按日分组_hour': '2023-10-09 00:00:00', '__$按日分组_minute': '2023-10-09 00:00:00', '__$按日分组_quarter': '2023-10-01 00:00:00', '__$按日分组_week': '2023-10-09 00:00:00', '__$按小时分组_year': '2023-01-01 00:00:00', '__$按小时分组_month': '2023-10-01 00:00:00', '__$按小时分组_day': '2023-10-09 00:00:00', '__$按小时分组_hour': '2023-10-09 14:00:00', '__$按小时分组_minute': '2023-10-09 14:00:00', '__$按小时分组_quarter': '2023-10-01 00:00:00', '__$按小时分组_week': '2023-10-09 00:00:00', '__$按分钟分组_year': '2023-01-01 00:00:00', '__$按分钟分组_month': '2023-10-01 00:00:00', '__$按分钟分组_day': '2023-10-09 00:00:00', '__$按分钟分组_hour': '2023-10-09 14:00:00', '__$按分钟分组_minute': '2023-10-09 14:47:00', '__$按分钟分组_quarter': '2023-10-01 00:00:00', '__$按分钟分组_week': '2023-10-09 00:00:00', '__$系统时间_year': '2023-01-01 00:00:00', '__$系统时间_month': '2023-10-01 00:00:00', '__$系统时间_day': '2023-10-09 00:00:00', '__$系统时间_hour': '2023-10-09 14:00:00', '__$系统时间_minute': '2023-10-09 14:47:00', '__$系统时间_quarter': '2023-10-01 00:00:00', '__$系统时间_week': '2023-10-09 00:00:00', '__$DATE1_year': '2023-01-01 00:00:00', '__$DATE1_month': '2023-06-01 00:00:00', '__$DATE1_day': '2023-06-19 00:00:00', '__$DATE1_hour': '2023-06-19 00:00:00', '__$DATE1_minute': '2023-06-19 00:00:00', '__$DATE1_quarter': '2023-04-01 00:00:00', '__$DATE1_week': '2023-06-19 00:00:00', '__$TODAY1_year': '2023-01-01 00:00:00', '__$TODAY1_month': '2023-10-01 00:00:00', '__$TODAY1_day': '2023-10-09 00:00:00', '__$TODAY1_hour': '2023-10-09 00:00:00', '__$TODAY1_minute': '2023-10-09 00:00:00', '__$TODAY1_quarter': '2023-10-01 00:00:00', '__$TODAY1_week': '2023-10-09 00:00:00', '按年分组': '2023', '按季度分组': '2023-04', '按月分组': '2023-10', '按周分组': '2023-42', '按日分组': '2023-10-09', '按小时分组': '2023-10-09 14', '按分钟分组': '2023-10-09 14:47', 'A1': 616.0, 'B1': 4337.536, 'G1': 56.0, 'ROUND1': 4337.5, 'ROUNDUP1': 4337.6, 'ROUNDDOWN1': 4337.5, 'SUM1': 4953.536, 'AVERAGE1': 2476.768, 'COUNT1': 2.0, 'COUNTA1': 2.0, 'MAX1': 4337.536, 'MEDIAN1': 2476.768, 'MIN1': 616.0, 'ABS1': 4337.536, 'max_B1': 4337.536, 'min_B1': 4337.536, '系统时间': '2023-10-09 14:47:59', 'DATE1': '2023-06-19 00:00:00', 'DATEDIF1': '1', 'DAY1': '9', 'DAYS1': '18', 'HOUR1': '14', 'MINUTE1': '47', 'MONTH1': '10', 'NOW1': '2023-10-09 14:48:48', 'SECOND1': '59', 'YEAR1': '2023', 'TODAY1': '2023-10-09 00:00:00', '差值年': 3.0, '差值月': 5.0, '差值天': 26.0, '差值时': 9.0, '差值分': 15.0, '差值秒': 20.0, 'H1': 'Abcf', 'CHAR1': '\\', 'CONCATENATE1': 'Abcf123', 'LEFT2': 'Ab', 'LEN1': '4', 'LOWER1': 'abcf', 'MID12': 'Ab', 'REPLACE1': '替换cf', 'RIGHT1': 'cf', 'TODATE1': '2023-06-19 00:00:00', 'TRIM1': 'Abcf', 'UPPER1': 'ABCF', '去空格后长度': '4', 'AND1': '0', 'FALSE1': '0', 'TRUE1': '1', 'IF1': '及格', 'NOT_true1': '0', 'NOT_false1': '1', 'OR1': '0'}]
    data= RequestUtil().replace_load(list_data5)
    print(data)



