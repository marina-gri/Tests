import pytest
import requests


@pytest.mark.xfail # убрать после добавления токена
class TestCreateFolderYandexAPI:
    def setup_method(self):
        self.headers = {
            'Authorization': 'OAuth <токен>'
        }

        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'

        self.params = {
            'path': 'Test_Folder'
        }

    def teardown_method(self):
        requests.delete(self.url,
                        params=self.params,
                        headers=self.headers)

    def test_create_folder_201(self):
        response = requests.put(self.url,
                                params=self.params,
                                headers=self.headers)
        assert response.status_code == 201
