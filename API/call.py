import requests
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
SERVER = 'http://alpha-api.lotuslms.com'

def send_api(school, type, url, payload):
    url = SERVER + url
    payload.update(school.param)
    rq = requests.request(type, url=url, data=payload, headers=HEADER)
    return rq.json()
