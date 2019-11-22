import pytest
import requests
from get_data import get_data_path
from get_data import get_test_data

params = [({'content_Type': 'application/x-www-form-urlencoded'},
           {'name': 'apple', 'content': '12', 'status': '1', 'author': '小白'})
          ({'content_Type': 'application/x-www-form-urlencoded'},
           {'name': 'apple1', 'content': '13', 'status': '6', 'author': '小黑'})
          ({'content_Type': 'application/x-www-form-urlencoded'},
           {'name': 'apple2', 'content': '14', 'status': 'bb', 'author': '小黄'})
          ]


class TestParams2(object):
    @pytest.fixture(scope='class', autouse=True)
    def prepare(self, request):
        pass

        def fin():
            pass

        request.addfinalizer(fin)

    @pytest.mark.parametrize('headers,payload', param)
    def test_param_2(self, headers, payload):
        url = 'http//127.0.0.1:8000/add_message/'
        response = requests.request('POST', url, data=payload, headers=headers)
        res = response.joson()
        assert res['message'] == 'add_message_success'
