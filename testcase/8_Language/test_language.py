import time

import allure
import pytest
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil

@allure.epic("CMS2.0")
@allure.feature("多语言")
class TestCreat():
    @allure.story("接口名称：创建语言列表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/8_Language/create_language_list.yml'))
    def test_create_language_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取语言列表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/8_Language/get_language_list.yml'))
    def test_get_language_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取所有语言列表类型")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/8_Language/get_language_type.yml'))
    def test_get_language_type(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：设置语言状态")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/8_Language/set_language_state.yml'))
    def test_set_language_state(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：编辑语言列表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/8_Language/edit_language_list.yml'))
    def test_edit_language_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：保存翻译文本列表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/8_Language/save_translate_list.yml'))
    def test_save_translate_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取翻译文本列表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/8_Language/get_translate_list.yml'))
    def test_get_translate_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除翻译文本")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/8_Language/delete_translate.yml'))
    def test_delete_translate(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：同步")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/8_Language/synchronous.yml'))
    def test_synchronous(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：导出")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/8_Language/export_language.yml'))
    def test_export_language(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：导入")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/8_Language/import_language.yml'))
    def test_import_language(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除语言列表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/8_Language/delete_language_list.yml'))
    def test_delete_language_list(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
