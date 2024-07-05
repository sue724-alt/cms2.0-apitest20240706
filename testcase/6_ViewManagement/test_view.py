import allure
import pytest
from common.parameters_util import read_testcase_file
from common.requests_util import RequestUtil

@allure.epic("CMS2.0")
@allure.feature("画面管理")
class TestCreat():
    @allure.story("接口名称：创建文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/create_view_folder.yml'))
    def test_create_view_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：编辑文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/edit_view_folder.yml'))
    def test_edit_view_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/delete_view_folder.yml'))
    def test_delete_view_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：移动文件夹")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/move_view_folder.yml'))
    def test_move_view_folder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：移动画面到文件夹下")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/move_viewtofolder.yml'))
    def test_move_viewtofolder(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建画面节点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/create_view.yml'))
    def test_create_view(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取画面节点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/get_view.yml'))
    def test_get_view(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取所有画面节点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/get_all_view.yml'))
    def test_get_all_view(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取画面节点树")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/get_view_tree.yml'))
    def test_get_view_tree(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取所有画面子节点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/get_child_node.yml'))
    def test_get_child_node(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：编辑画面节点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/edit_view.yml'))
    def test_edit_view(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除画面节点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/delete_view.yml'))
    def test_delete_view(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：批量删除画面节点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/batch_delete_view.yml'))
    def test_batch_delete_view(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：移动画面节点")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/move_view.yml'))
    def test_move_view(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取首页id")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/get_home_view_id.yml'))
    def test_get_home_view_id(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：设置首页")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/set_home_view.yml'))
    def test_set_home_view(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取首页")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/get_home_view.yml'))
    def test_get_home_view(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：创建图库组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/create_gallery_group.yml'))
    def test_create_gallery_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取图库树")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/get_gallery_tree.yml'))
    def test_get_gallery_tree(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：重命名图库组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/rename_gallery_group.yml'))
    def test_rename_gallery_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：获取分组的结构")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/get_gallery_group.yml'))
    def test_get_gallery_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除图库组")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/delete_gallery_group.yml'))
    def test_delete_gallery_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：上传图片")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/upload_picture.yml'))
    def test_upload_picture(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：删除图片")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/delete_picture.yml'))
    def test_delete_picture(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：下载图片")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/download_picture.yml'))
    def test_download_picture(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：导出图片")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/download_gallery_group.yml'))
    def test_download_gallery_group(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)

    @allure.story("接口名称：搜索图片")
    @pytest.mark.parametrize('caseinfo', read_testcase_file('/testcase/6_ViewManagement/search_for_picture.yml'))
    def test_search_for_picture(self, caseinfo):
        allure.dynamic.title(caseinfo['name'])
        allure.dynamic.description(caseinfo['name'])
        RequestUtil().analysis_yaml(caseinfo)