import allure
import pytest
import time
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil

@allure.epic("CMS2.0")
@allure.feature("数据管理")
class TestCreat():
    @allure.story("接口名称：获取数据管理配置树")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_tree.yml'))
    def test_view(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建文件夹(后续删除)")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_folder.yml'))
    def test_create_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取所有文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_folder.yml'))
    def test_get_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：重命名文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/rename_folder.yml'))
    def test_rename_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/delete_folder.yml'))
    def test_delete_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建文件夹2")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_folder.yml'))
    def test_create_folder2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
    @allure.story("接口名称：创建归档表（后续删除）")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_original_table.yml'))
    def test_create_original_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取归档表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_original_table.yml'))
    def test_get_original_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：重命名归档表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/rename_original_table.yml'))
    def test_rename_original_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除归档表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/delete_original_table.yml'))
    def test_delete_original_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建归档表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_original_table.yml'))
    def test_create_original_table2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：设置归档表字段配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_original_table_fields.yml'))
    def test_create_original_field(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取归档表字段配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_original_table_fields.yml'))
    def test_get_original_field(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：设置归档表触发配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_original_table_trigger.yml'))
    def test_create_original_table_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：异常设置归档表触发配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_original_table_trigger_error.yml'))
    def test_create_original_table_trigger_error(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取归档表触发配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_original_table_trigger.yml'))
    def test_get_original_table_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取归档表表头字段设置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_original_table_header_fields.yml'))
    def test_get_original_table_header_fields(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建聚合表后续删除")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_aggregate_table.yml'))
    def test_create_aggregate_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取聚合表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_aggregate_table.yml'))
    def test_get_aggregate_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取所有聚合表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_all_aggregate_table.yml'))
    def test_get_all_aggregate_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：编辑聚合表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/edit_aggregate_table.yml'))
    def test_edit_aggregate_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：重命名聚合表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/rename_aggregate_table.yml'))
    def test_rename_aggregate_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除聚合表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/delete_aggregate_table.yml'))
    def test_delete_aggregate_table(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建聚合表")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_aggregate_table.yml'))
    def test_create_aggregate_table2(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：通过聚合表获取归档表字段")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_originaltable_fields_through_aggregatetale.yml'))
    def test_get_originaltable_fields_through_aggregatetale(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：设置聚合表字段配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_aggregate_table_fields.yml'))
    def test_create_aggregate_table_fields(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取聚合表字段配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_aggregate_table_fields.yml'))
    def test_get_aggregate_table_fields(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：设置聚合表触发配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_aggregate_table_trigger.yml'))
    def test_create_aggregate_table_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：聚合表触发异常配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_aggregate_table_trigger_error.yml'))
    def test_create_aggregate_table_trigger_error(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取聚合表触发异常配置")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_aggregate_table_trigger.yml'))
    def test_get_aggregate_table_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取聚合表表头字段")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/5_DataManagement/get_aggregate_table_header_fields.yml'))
    def test_get_aggregate_table_header_fields(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：实时缓存配置")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/5_DataManagement/create_cache_configuration.yml'))
    def test_create_cache_configuration(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：归档表实时缓存配置-缓存容量为空情况")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/5_DataManagement/create_cache_configuration_error.yml'))
    def test_create_cache_configuration_error(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：字段配置删除警告")
    @pytest.mark.parametrize('caseinfo',read_testcase_file('/testcase/5_DataManagement/delete_fields_warning.yml'))
    def test_delete_fields_warning(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：查询删除警告")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/query_delete_warning.yml'))
    def test_query_delete_warning(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建副本")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/create_a_copy.yml'))
    def test_create_a_copy(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取节点信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_node_info.yml'))
    def test_get_node_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取字段信息")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/get_fields_info.yml'))
    def test_get_fields_info(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：排序")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/set_sorting.yml'))
    def test_set_sorting(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：排序+拖拽")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/set_drag_sorting.yml'))
    def test_set_drag_sorting(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    # =============================场景用例========================================
    # 归档表-定时触发
    @allure.story("接口名称：归档表-定时触发")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/original_table_timing_trigger.yml'))
    def test_original_table_timing_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：归档表-变量触发")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/5_DataManagement/original_table_var_trigger.yml'))
    def test_original_table_var_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：归档表-字段触发")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/5_DataManagement/original_table_field_trigger.yml'))
    def test_original_table_field_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：归档表-变化触发")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/5_DataManagement/original_table_change_trigger.yml'))
    def test_original_table_change_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：归档表-报警触发")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/5_DataManagement/original_table_alarm_trigger.yml'))
    def test_original_original_table_alarm_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：聚合表-实时触发")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/5_DataManagement/aggregate_table_real_time_trigger.yml'))
    def test_aggregate_table_real_time_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：聚合表-定时触发")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/5_DataManagement/aggregate_table_timing_trigger.yml'))
    def test_aggregate_table_timing_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：聚合表-变量触发")
    @pytest.mark.parametrize('caseinfo',
                             read_testcase_file('/testcase/5_DataManagement/aggregate_table_var_trigger.yml'))
    def test_aggregate_table_var_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：启动数据服务")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/start_data_service.yml'))
    def test_start_data_service(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：启动报警服务")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/start_alarm_service.yml'))
    def test_start_alarm_service(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称: 下发变量A1")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/write_cms_io_var.yml'))
    def test_write_cms_io_var(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：查询数据(归档表-定时触发)")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/query_data(original_table_timing_trigger).yml'))
    def test_query_data_original_table_timing_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：查询数据(归档表-字段触发)")
    @pytest.mark.parametrize('caseinfo', read_testcase_file(
        '/testcase/5_DataManagement/query_data(original_table_field_trigger).yml'))
    def test_query_data_original_table_field_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：查询数据(归档表-变量触发)")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/query_data(original_table_var_trigger).yml'))
    def test_query_data_original_table_var_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：查询数据(归档表-变化触发)")
    @pytest.mark.parametrize('caseinfo', read_testcase_file(
        '/testcase/5_DataManagement/query_data(original_table_change_trigger).yml'))
    def test_query_data_original_table_change_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：查询数据(归档表-报警触发)")
    @pytest.mark.parametrize('caseinfo', read_testcase_file(
        '/testcase/5_DataManagement/query_data(original_table_alarm_trigger).yml'))
    def test_query_data_original_table_alarm_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(2)

    @allure.story("接口名称：查询数据(实时聚合表)")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/query_data(aggregate_table_real_timing_trigger).yml'))
    def test_query_data_aggregate_table_real_timing_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(10)
        time.sleep(62)

    @allure.story("接口名称：查询数据(定时聚合表)")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/query_data(aggregate_table_timing_trigger).yml'))
    def test_query_data_aggregate_table_timing_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(10)

    @allure.story("接口名称：查询数据(变量触发聚合表)")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/query_data(aggregate_table_var_trigger).yml'))
    def test_query_data_aggregate_table_var_trigger(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)
        time.sleep(10)

    #--------------------------
    @allure.story("接口名称：数据备份")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/data_backup.yml'))
    def test_data_backup(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：数据清除")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/5_DataManagement/data_dump.yml'))
    def test_data_dump(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)






