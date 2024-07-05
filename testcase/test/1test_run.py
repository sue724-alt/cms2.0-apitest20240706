import allure
import pytest
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil
@allure.epic("cms2.0")
@allure.feature("工程管理")
class TestCreat():
    @allure.story("接口名称：获取鉴权码")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/test/get_Authorization.yaml'))
    def test_get_Authorization(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：新建工程")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/test/create_project.yaml'))
    def test_create_project(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取工程信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/test/get_project_info.yaml'))
    def test_project_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：图片上传")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/test/upload_image.yaml'))
    def test_upload_image(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：变量下发")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/test/variable_write.yaml'))
    def test_variable_write(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)