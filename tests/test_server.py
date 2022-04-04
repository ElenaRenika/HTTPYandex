import pytest
from requests import Request, Session
import logging

logger = logging.basicConfig(level=logging.DEBUG)
	
@pytest.mark.parametrize("redirects, http_code", [
    (False, 302),
    (True, 200), 
])

def test_answer_code(http_request, redirects, http_code):
    http_request.get_response(allow_redirects=redirects) 
    assert http_request.status_code == http_code
    
