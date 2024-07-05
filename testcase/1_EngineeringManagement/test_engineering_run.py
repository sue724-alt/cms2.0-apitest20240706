import allure
import pytest
import time
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil

@allure.epic("CMS2.0")
@allure.feature("工程管理")
class TestCreat():
    @allure.story("接口名称：重命名工程")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/1_EngineeringManagement/rename_project.yml'))
    def test_rename_project(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(5)

    @allure.story("接口名称：创建工程")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/1_EngineeringManagement/creat_project.yml'))
    def test_creat_project(self,caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/1_EngineeringManagement/creat_folder.yml'))
    def test_creat_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取工程信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/1_EngineeringManagement/get_project_info.yml'))
    def test_get_project_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    # 执行重命名脚本会导致其他脚本执行失败，暂时不写

    @allure.story("接口名称：获取工程树节点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/1_EngineeringManagement/get_project_tree.yml'))
    def test_get_project_tree(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：移动工程到文件夹下")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/1_EngineeringManagement/move_project.yml'))
    def test_move_project(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除工程并保留路径下的文件")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/1_EngineeringManagement/delete_project_pathreserve.yml'))
    def test_delete_project_pathreserve(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除工程并删除路径下的文件")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/1_EngineeringManagement/delete_project_pathdelete.yml'))
    def test_delete_project_pathdelete(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除文件夹")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/1_EngineeringManagement/delete_folder.yml'))
    def test_delete_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建工程副本")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/1_EngineeringManagement/copy_project.yml'))
    def test_copy_project(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：查询")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/1_EngineeringManagement/find_node.yml'))
    def test_find_node(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：刷新列表")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/1_EngineeringManagement/refresh_node.yml'))
    def test_refresh_node(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：导入本地工程文件")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/1_EngineeringManagement/import_local_project.yml'))
    def test_import_local_project(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：导入远程工程文件")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/1_EngineeringManagement/import_remote_project.yml'))
    def test_import_remote_project(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取当前软件版本")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/1_EngineeringManagement/get_version.yml'))
    def test_get_version(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：升级工程版本")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/1_EngineeringManagement/upgrade_project_version.yml'))
    def test_upgrade_project_version(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：比对工程id")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/1_EngineeringManagement/check_project_different_id.yml'))
    def test_check_prject_id(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：数据恢复")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/1_EngineeringManagement/data_recovery.yml'))
    def test_data_recovery(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：备份工程")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/1_EngineeringManagement/data_backup.yml'))
    def test_data_backup(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：获取鉴权码")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/1_EngineeringManagement/get_requesttoken.yml'))
    def test_get_requesttoken(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(5)
