from requests import Request, Session

class BaseRequest(object):

    def __init__(self, url):
        self.url = url
        self.session = Session()

    def create_session(self, url):
        s = session = self.session
        s.url = url
        self.session = session
        return self.session

    def get_response(self, method='GET', **param):
        s = self.session
        self.allow_redirects = param.get('allow_redirects', None)

        req = Request(method, url=self.url)
        prepped = s.prepare_request(req)
        self.response = s.send(prepped, allow_redirects=self.allow_redirects)

        self.status_code = self.response.status_code
