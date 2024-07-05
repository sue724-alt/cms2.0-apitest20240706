import logging
import time

from common.yaml_util import get_object_path, read_config_file


class LoggerUtil:
    def creat_log(self,logger_name='log'):
        #创建一个日志对象
        self.logger = logging.getLogger(logger_name)
        #设置全局的日志级别（critical>error>waring>info>debug）
        self.logger.setLevel(logging.DEBUG)
        #放置日志重复
        if not self.logger.handlers:
            #-----------文件日志----------
            #获得日志文件的名称
            self.file_log_path = get_object_path()+'/logs/'+ read_config_file('log','log_name')+str(int(time.time()))+'.log'
            # print(self.file_log_path)
            #创建文件日志的控制器
            self.file_hander = logging.FileHandler(self.file_log_path,encoding='utf-8')
            #设置文件日志的界别
            file_log_lever = str(read_config_file('log','log_level')).lower()
            if file_log_lever =='debug':
                self.file_hander.setLevel(logging.DEBUG)
            elif file_log_lever =='info':
                self.file_hander.setLevel(logging.INFO)
            elif file_log_lever =='warning':
                self.file_hander.setLevel(logging.WARNING)
            elif file_log_lever =='error':
                self.file_hander.setLevel(logging.ERROR)
            elif file_log_lever == 'critical':
                self.file_hander.setLevel(logging.CRITICAL)
            #设置文件日志的格式
            self.file_hander.setFormatter(logging.Formatter(read_config_file('log','log_format')))
            #将控制器加入到日志对象
            self.logger.addHandler(self.file_hander)

            #-----------控制台日志----------
            # 创建控制台日志的控制器
            self.console_hander = logging.StreamHandler()
            # 设置控制台日志的界别
            console_log_lever = str(read_config_file('log', 'log_level')).lower()
            if console_log_lever == 'debug':
                self.console_hander.setLevel(logging.DEBUG)
            elif console_log_lever == 'info':
                self.file_hander.setLevel(logging.INFO)
            elif console_log_lever == 'warning':
                self.console_hander.setLevel(logging.WARNING)
            elif console_log_lever == 'error':
                self.console_hander.setLevel(logging.ERROR)
            elif console_log_lever == 'critical':
                self.console_hander.setLevel(logging.CRITICAL)
            # 设置控制台日志的格式
            self.console_hander.setFormatter(logging.Formatter(read_config_file('log', 'log_format')))
            # 将控制器加入到日志对象
            self.logger.addHandler(self.console_hander)
        return self.logger

#函数：输出正常日志
def write_log(log_message):
    LoggerUtil().creat_log().info(log_message)

#函数：输出错误日志
def error_log(log_message):
    LoggerUtil().creat_log().info(log_message)
    raise Exception(log_message)
