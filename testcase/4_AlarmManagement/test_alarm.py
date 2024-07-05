import time

import allure
import pytest
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil
from common.yaml_util import read_extract_file, read_config_file
from debug_talk import DubugTalk

@allure.epic("CMS2.0")
@allure.feature("报警管理")
class TestCreat():

    @allure.story("接口名称：创建报警文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/create_alarm_folder.yml'))
    def test_create_alarm_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建报警组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/create_alarm_group.yml'))
    def test_create_alarm_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：更新报警文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/update_alarm_folder.yml'))
    def test_update_alarm_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：更新报警组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/update_alarm_group.yml'))
    def test_update_alarm_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：查询报警组树")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/get_alarm_tree.yml'))
    def test_get_alarm_tree(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除报警文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/delete_alarm_folder.yml'))
    def test_delete_alarm_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除报警组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/delete_alarm_group.yml'))
    def test_delete_alarm_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建报警组2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/create_alarm_group.yml'))
    def test_create_alarm_group2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建报警等级")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/create_alarm_grade.yml'))
    def test_create_alarm_grade(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：更新报警等级")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/update_alarm_grade.yml'))
    def test_update_alarm_grade(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：查询报警等级")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/get_alarm_grade.yml'))
    def test_get_alarm_grade(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除报警等级")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/delete_alarm_grade.yml'))
    def test_delete_alarm_grade(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建报警等级2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/create_alarm_grade.yml'))
    def test_create_alarm_grade2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建报警类别组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/create_alarm_category.yml'))
    def test_create_alarm_category(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：更新报警类别组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/update_alarm_category.yml'))
    def test_update_alarm_category(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除报警类别组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/delete_alarm_category.yml'))
    def test_delete_alarm_category(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建报警类别组2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/create_alarm_category.yml'))
    def test_create_alarm_category2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：查询报警类别组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/get_alarm_category.yml'))
    def test_get_alarm_category(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建报警类别项")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/create_alarm_category_item.yml'))
    def test_create_alarm_category_item(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：更新报警类别项")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/4_AlarmManagement/update_alarm_category_item.yml'))
    def test_update_alarm_category_item(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取报警类别项")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/4_AlarmManagement/get_alarm_category_item.yml'))
    def test_get_alarm_category_item(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建报警点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/create_alarm_point.yml'))
    def test_create_alarm_point(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：更新报警点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/update_alarm_point.yml'))
    def test_update_alarm_point(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：查询报警点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/get_alarm_point.yml'))
    def test_get_alarm_point(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除报警点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/delete_alarm_point.yml'))
    def test_delete_alarm_point(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建报警点2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/create_alarm_point.yml'))
    def test_create_alarm_point2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：导出报警点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/export_alarm.yml'))
    def test_export_alarm(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：启动报警服务")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/start_alarm_service.yml'))
    def test_start_alarm_service(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(1)

    @allure.story("接口名称：下发变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/write_cms_io_var.yml'))
    def test_write_cms_io_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(3)

    @allure.story("接口名称：查询实时报警表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/4_AlarmManagement/query_real_time_alarm_table.yml'))
    def test_query_real_time_alarm_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(5)

    @allure.story("接口名称：查询历史报警表")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/4_AlarmManagement/query_history_alarm_table.yml'))
    def test_query_history_alarm_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(5)

    @allure.story("接口名称：清空数据")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/4_AlarmManagement/data_dump.yml'))
    def test_data_dump(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
