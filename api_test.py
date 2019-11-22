import pytest
import requests

par_to_test = [{'case': 'search for a word:haha',
                'headers': {},
                'querystring': {'wd': 'haha'},
                'payload': {},
                'expected': {'status_code': 200}
                },
               {'case': 'search for a word2:kuku',
                'headers': {},
                'querystring': {'wd': 'kuku'},
                'payload': {},
                'expected': {'status_code': 200}
                },
               ]


@pytest.fixture(params=par_to_test)
def class_scope(request):
    return request.params


def test_baidu_search(class_scope):
    url = 'https://www.baidu.com'
    r = requests.request('GET', url, data=class_scope['payload'], headers=class_scope['headers'],
                         params=class_scope['querystring'])
    assert r.status_code == class_scope['expected']['status_code']
