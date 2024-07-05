import allure
import pytest
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil

@allure.epic("SIOT")
@allure.feature("modbus协议变量读写")
class TestCreat():
    @allure.story("接口名称：变量下发")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/ModBus/modbus_write.yml'))
    def test_modbus_write(self,caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：变量读取")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/ModBus/modbus_read.yml'))
    def test_modbus_read(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)