import pytest

@pytest.fixture(autouse=True)
def get_url():
    pass

@pytest.fixture()
def init():
    pass

cases = []
@pytest.mark.parametrize('a,b,expect',cases)
def test_sign():
    pass

if __name__=='__main__':
    pytest.main(['-v','--tb=short','--html=signup.html','sign.py'])