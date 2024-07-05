import allure
import pytest
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil

@allure.epic("CMS2.0")
@allure.feature("基础管理")
class TestCreat():
    @allure.story("接口名称：创建跨天班次")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/2_BasicManagement/creat_classes.yml'))
    def test_creat_classes(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取班次配置")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/2_BasicManagement/get_classes_info.yml'))
    def test_get_classes_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建班次-开始时间不可大于结束时间")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/2_BasicManagement/Start_time_gt_end_time.yml'))
    def test_Start_time_gt_end_time(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建班次-班次开始时间不能小于上一个班次结束时间")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/2_BasicManagement/Start_time_lt_classes_end_time.yml'))
    def test_Start_time_lt_classes_end_time(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)