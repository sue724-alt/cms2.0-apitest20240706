import allure
import pytest
import time
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil
class TestCreat():
    @allure.story("接口名称：开启互联服务")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/start_internet_services.yml'))
    def test_start_internet_services(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：测试连接互联项")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/test_interconnection.yml'))
    def test_testinterconnection(self, caseinfo,create_mysqldb_fixture):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：创建互联项")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/create_interconnection.yml'))
    def test_create_interconnection(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：关闭互联项")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/stop_interconnection.yml'))
    def test_stop_interconnection(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：开启互联项")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/start_interconnection.yml'))
    def test_start_interconnection(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：重命名互联项")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/rename_interconnection.yml'))
    def test_rename_interconnection(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：修改互联配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/edit_interconnection.yml'))
    def test_edit_interconnection(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除互联项")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/delete_interconnection.yml'))
    def test_delete_interconnection(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建互联项2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/create_interconnection.yml'))
    def test_create_interconnection2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建映射表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/create_mapping_table.yml'))
    def test_create_mapping_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：禁用映射表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/stop_mapping_table.yml'))
    def test_stop_mapping_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：开启映射表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/start_mapping_table.yml'))
    def test_start_mapping_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：重命名映射表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/rename_mapping_table.yml'))
    def test_rename_mapping_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取映射表配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/get_mapping_table_config.yml'))
    def test_get_mapping_table_config(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：映射表创建副本")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/copy_mapping_table.yml'))
    def test_copy_mapping_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除映射表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/delete_mapping_table.yml'))
    def test_delete_mapping_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：预览数据表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/data_table_preview.yml'))
    def test_data_table_preview(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：保存配置-插入")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/save_config.yml'))
    def test_save_config(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：下发变量1")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/write_var.yml'))
    def test_write_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：执行插入语句")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/execute_insert.yml'))
    def test_execute_insert(self, caseinfo,truncate_mysqldb_fixture):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：插入-刷新")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/refresh_insert.yml'))
    def test_refresh(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：执行查询语句")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/execute_query.yml'))
    def test_execute_query(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(1)

    @allure.story("接口名称：查询-刷新")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/refresh_query.yml'))
    def test_refresh_query(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(1)

    @allure.story("接口名称：下发变量2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/write_var2.yml'))
    def test_write_var2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：执行修改语句")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/execute_modify.yml'))
    def test_execute_modify(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(1)

    @allure.story("接口名称：修改-刷新")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/refresh_modify.yml'))
    def test_refresh_modify(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(1)

    @allure.story("接口名称：下发变量3")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/write_var3.yml'))
    def test_write_var3(self, caseinfo,truncate_mysqldb_fixture):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：定时触发-插入")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/insert_time_triggered.yml'))
    def test_insert_time_triggered(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(5)

    @allure.story("接口名称：禁用-定时插入映射表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/stop_time_mapping_table.yml'))
    def test_stop_time_mapping_table(self, caseinfo,truncate_mysqldb_fixture):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：变量触发-插入")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/insert_var_triggered.yml'))
    def test_insert_var_triggered(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(5)

    @allure.story("接口名称：禁用-变量触发映射表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/stop_var_mapping_table.yml'))
    def test_stop_var_mapping_table(self, caseinfo, truncate_mysqldb_fixture):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：报警触发-插入")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/insert_alarm_triggered.yml'))
    def test_insert_alarm_triggered(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(5)

    @allure.story("接口名称：禁用报警触发映射表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/9_Interconnection/stop_alarm_mapping_table.yml'))
    def test_stop_alarm_mapping_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(5)

