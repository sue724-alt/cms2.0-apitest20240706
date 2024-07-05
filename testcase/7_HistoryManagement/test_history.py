import time

import allure
import pytest
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil

@allure.epic("CMS2.0")
@allure.feature("历史管理")
class TestCreat():
    @allure.story("接口名称：创建历史文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/create_history_folder.yml'))
    def test_create_history_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：编辑历史文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/edit_history_folder.yml'))
    def test_edit_history_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除历史文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/delete_history_folder.yml'))
    def test_delete_history_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建历史组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/create_history_group.yml'))
    def test_create_history_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：编辑历史组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/edit_history_group.yml'))
    def test_edit_history_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除历史组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/delete_history_group.yml'))
    def test_delete_history_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取历史组树")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/get_history_tree.yml'))
    def test_get_history_tree(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取所有历史组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/get_history_group.yml'))
    def test_get_history_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取变量信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/get_tunnel_var_info.yml'))
    def test_get_tunnel_var_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：添加历史组变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/create_history_var.yml'))
    def test_create_history_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取历史组变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/get_history_var.yml'))
    def test_get_history_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除历史组变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/delete_history_var.yml'))
    def test_delete_history_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：添加历史组变量2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/create_history_var.yml'))
    def test_create_history_var2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
#--------------------------------------定时触发--------------------------------------------
    @allure.story("接口名称：设置归档配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/set_archive_configuration.yml'))
    def test_set_archive_configuration(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取归档配置")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/7_HistoryManagement/get_archive_configuration.yml'))
    def test_get_archive_configuration(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：配置存储设置")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/7_HistoryManagement/save_setting.yml'))
    def test_save_setting(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取存储设置")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/7_HistoryManagement/get_save_setting.yml'))
    def test_get_save_setting(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：下发io变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/write_cms_io_var.yml'))
    def test_write_cms_io_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(0.5)

    @allure.story("接口名称：开启历史归档服务")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/start_history_service.yml'))
    def test_start_history_service(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(5)

    @allure.story("接口名称：查询历史数据")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/7_HistoryManagement/query_history(time_trigger).yml'))
    def test_query_history_time_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：备份历史数据")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/backup_historical_data.yml'))
    def test_backup_historical_data(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：移动变量到其他变量组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/backup_historical_data.yml'))
    def test_backup_historical_data(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

 # --------------------------------------变化触发，绝对值--------------------------------------------
    @allure.story("接口名称：关闭历史归档")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/stop_history_service.yml'))
    def test_stop_history_service(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：清除历史数据")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/clear_historical_data.yml'))
    def test_clear_historical_data(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(3)

    @allure.story("接口名称：配置变化触发-绝对值")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/change_trigger(absolute).yml'))
    def test_change_trigger_absolute(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：开启历史归档服务2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/start_history_service.yml'))
    def test_start_history_service2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(3)

    @allure.story("接口名称：下发io变量2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/write_cms_io_var2.yml'))
    def test_write_cms_io_var2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：查询历史数据（变化触发-绝对值）")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/query_history(change_trigger_absolute).yml'))
    def test_query_history_change_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

# --------------------------------------变化触发，百分比--------------------------------------------
    @allure.story("接口名称：关闭历史归档2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/stop_history_service.yml'))
    def test_stop_history_service2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：清除历史数据2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/clear_historical_data.yml'))
    def test_clear_historical_data2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(3)

    @allure.story("接口名称：配置变化触发-百分比")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/change_trigger(percentage).yml'))
    def test_change_trigger_percentage(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：开启历史归档服务3")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/start_history_service.yml'))
    def test_start_history_service3(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(3)

    @allure.story("接口名称：下发io变量3")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/write_cms_io_var3.yml'))
    def test_write_cms_io_var3(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：查询历史数据（变化触发-百分比）")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/7_HistoryManagement/query_history(change_trigger_percentage).yml'))
    def test_query_history_change_trigger_percentage(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

