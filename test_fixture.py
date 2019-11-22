import pytest


@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    assert some_data == 42


@pytest.fixture()
def a_list():
    return [1, 2, 3, 4, 5]


def test_a_list():
    assert a_list[2] == 3


# class级别
@pytest.fixture(scope='class')
def first():
    print('获取用户名，scope为class级别只运行一次')
    a = 'Mr.Zhu'
    return a


class Testcase():
    def test1(self, first):
        assert first == 'Mr.Zhu'

    def test2(self, first):
        assert first == 'Mr.Zhu'


# module级别
@pytest.fixture(scope='module')
def first():
    print('获取用户名，scope为module级别，程序运行一次')
    a = '朱先生'
    return a


def test_1(first):
    assert first == '朱先生'


class Testcase1():
    def test_2(self, first):
        assert first == '朱先生'


# session级别
@pytest.fixture(scope='session')
def first():
    print('获取用户名，scope为module级别，程序运行一次')
    a = '朱先生'
    return a
