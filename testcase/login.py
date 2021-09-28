import pytest

@pytest.fixture(autouse=True)
def get_url():
    pass

@pytest.fixture()
def init():
    pass
@pytest.fixture()
def init1():
    pass

cases = []
@pytest.mark.parametrize('a,b,expect',cases)
def test_login():
    pass

if __name__=='__main__':
    pytest.main(['-v','--tb=short','--html=login.html','login.py'])