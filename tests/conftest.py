import pytest
from Request import BaseRequest

URL = 'http://yandex.ru'

@pytest.yield_fixture(scope="session")
def http_request():
    request =  BaseRequest(URL)
    yield request

