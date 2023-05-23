import requests
import json
import urllib3
urllib3.disable_warnings()
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

SERVER = 'http://alpha-api.lotuslms.com'
PW = 'qwe123!@#QWE'


def login(self, user, pw=PW):
    payload = {'lname': user, 'pass': pw}
    r = self.send('POST', '/user/login', payload)
    try:
        r = r['result']
        info = {'_sand_token': r['token'],'_sand_uiid': r['iid'], '_sand_uid': r['id']}
        self.param.update(info)
        print(f"Đã login bằng tài khoản: {user}")
        return r
    except:
        pass

class Domain:
    def __init__(self, domain, user, SV = SERVER, pw=PW):
        self.param = {'submit': '1', '_sand_ajax': '1', '_sand_platform': '3', '_sand_readmin': '1', '_sand_is_wan': 'false',
                      '_sand_ga_sessionToken': '', '_sand_ga_browserToken': '', '_sand_domain': domain, '_sand_masked': ''}
        self.server = SV 
        self.user = login(self,user, pw)
        self.url = 'https://'+domain+'.lotuslms.com'
        

    def send(self,type, url, payload, files =[]):
        
        url = self.server + url
        payload.update(self.param)
        rq = requests.request(type, url=url, data=payload, headers=HEADER, files =files, verify=False)
        return rq.json()

def upload(self,path):
    payload ={}
    files = {'file': open(path, 'rb')}
    r = self.send('POST', '/file/upload', payload, files=files)
    link = r['result']['attachments'][0]['link']
    print(f">>> Uploaded: {link}")
    return link
