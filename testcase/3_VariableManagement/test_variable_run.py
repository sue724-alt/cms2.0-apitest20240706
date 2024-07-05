import allure
import pytest
import time
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil

@allure.epic("CMS2.0")
@allure.feature("变量管理")
class TestCreat():
    @allure.story("接口名称：获取协议信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/get_protocol_info.yml'))
    def test_get_protocol_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建通道")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/creat_tunnel.yml'))
    def test_creat_tunnel(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建通道-后续删除")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/creat_tunnel1.yml'))
    def test_creat_tunnel_repeat(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：校验通道配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/check_tunnel.yml'))
    def test_creat_tunnel_check(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除通道1")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/delete_tunnel1.yml'))
    def test_delete_tunnel_repeat(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取所有通道")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/get_all_tunnel.yml'))
    def test_get_all_tunnel(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取通道信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/get_tunnel_info.yml'))
    def test_get_tunnel_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：禁用通道")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/disable_tunnel.yml'))
    def test_disable_tunnel(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：启用通道")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/enable_tunnel.yml'))
    def test_enable_tunnel(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：校验变量组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/check_io_group.yml'))
    def test_check_io_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建变量组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/creat_io_group.yml'))
    def test_creat_io_var_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：重命名变量组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/rename_io_group.yml'))
    def test_rename_io_var_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取通道下所有io变量组信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/get_all_io_group_info.yml'))
    def test_get_all_io_var_group_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取io变量组信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/rename_io_group.yml'))
    def test_rename_io_var_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除io变量组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/delete_io_group.yml'))
    def test_delete_io_var_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建变量组1")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/creat_io_group.yml'))
    def test_creat_io_var_group1(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：添加io变量(供删除)")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/creat_io_variable_to_del.yml'))
    def test_creat_io_variable(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取变量信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/get_io_var_info.yml'))
    def test_get_io_var_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取通道下所有变量信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/get_tunnel_var_info.yml'))
    def test_get_tunnel_var_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：校验io变量配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/check_io_variable.yml'))
    def test_check_io_variable(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除io变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/delete_io_variable.yml'))
    def test_delete_io_variable(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：编辑io变量信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/edit_io_variable.yml'))
    def test_edit_io_variable(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：批量删除io变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/batch_delete_io_variable.yml'))
    def test_batch_delete_io_variable(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：添加所有类型的变量")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/3_VariableManagement/creat_io_variable.yml'))
    def test_creat_io_variable2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取服务信息")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/3_VariableManagement/get_service_info.yml'))
    def test_get_service_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：指定变量服务")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/3_VariableManagement/get_var_service.yml'))
    def test_get_var_service(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @pytest.mark.flaky(reruns=5)
    @allure.story("接口名称：启动变量服务")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/3_VariableManagement/start_var_service.yml'))
    def test_start_var_service(self, caseinfo):
        RequestUtil().analysis_yaml(caseinfo)
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])

    @allure.story("接口名称：异常下发io变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/write_cms_io_var_error.yml'))
    def test_write_cms_io_var_error(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(0.3)

    @allure.story("接口名称：下发io变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/write_cms_io_var.yml'))
    def test_write_cms_io_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(1)

    @allure.story("接口名称：读取io变量")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/3_VariableManagement/read_cms_io_var.yml'))
    def test_read_cms_io_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(1)
# =====================================================内部变量===========================================================
    @allure.story("接口名称：校验内部通道必填项")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/check_inner_tunnel.yml'))
    def test_check_inner_tunnel(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建内部变量通道")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/creat_inner_tunnel.yml'))
    def test_creat_inner_tunnel(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：编辑内部通道")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/edit_inner_tunnel.yml'))
    def test_edit_inner_tunnel(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：校验内部变量组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/check_inner_group.yml'))
    def test_check_inner_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建内部变量组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/creat_inner_group.yml'))
    def test_creat_inner_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建内部变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/creat_inner_variable_to_del.yml'))
    def test_creat_inner_variable_to_del(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：校验内部变量必填项")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/3_VariableManagement/check_inner_variable.yml'))
    def test_check_inner_variable(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除内部变量ee1")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/delete_inner_variable.yml'))
    def test_delete_inner_variable(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建内部变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/creat_inner_variable.yml'))
    def test_creat_inner_variable(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：异常下发内部变量")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/3_VariableManagement/write_cms_inner_var_error.yml'))
    def test_write_cms_inner_var_error(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(0.2)

    @allure.story("接口名称：下发内部变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/write_cms_inner_var.yml'))
    def test_write_cms_inner_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(0.5)

    @allure.story("接口名称：读取内部变量")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/3_VariableManagement/read_cms_inner_var.yml'))
    def test_read_cms_inner_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    # @allure.story("接口名称：为数据管理下发变量")
    # @pytest.mark.parametrize('caseinfo',
    #                          read_testcase_file('/testcase/3_VariableManagement/write_cms_var_fordata.yml'))
    # def test_write_cms_inner_var_fordata(self, caseinfo):
    #     allure.dynamic.title(caseinfo['name'])
    #     allure.dynamic.description(caseinfo['name'])
    #     RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：读取系统变量")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/3_VariableManagement/read_system_var.yml'))
    def test_read_system_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建io映射通道")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/creat_mapping_tunnel.yml'))
    def test_creat_mapping_tunnel(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：添加io映射变量")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/creat_io_mapping_variable.yml'))
    def test_creat_io_mapping_variable(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：下发io映射变量")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/3_VariableManagement/write_io_mapping_var.yml'))
    def test_write_io_mapping_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(1)

    @allure.story("接口名称：读取io映射变量")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/3_VariableManagement/read_cms_io_mapping_var.yml'))
    def test_read_cms_io_mapping_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(1)
    #----------------
    @allure.story("接口名称：创建逻辑变量通道")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/3_VariableManagement/creat_logic_var_tunnel.yml'))
    def test_creat_logic_var_tunnel(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：添加逻辑变量")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/3_VariableManagement/creat_logic_var.yml'))
    def test_creat_logic_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：读取逻辑变量")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/3_VariableManagement/read_logic_var.yml'))
    def test_read_cms_logic_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(1)
