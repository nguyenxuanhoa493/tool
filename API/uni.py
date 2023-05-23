import requests
import json
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
SERVER = 'https://center-api.smartlms.vn'
PW = 'uni123'
RANGE_TIME = {
    'Sáng':{'scheduled[start_time]': '450','scheduled[end_time]': '690','learn_duration':'240'},
    'Chiều':{'scheduled[start_time]': '780','scheduled[end_time]': '1020','learn_duration':'240'},
    'Tối':{'scheduled[start_time]': '1140','scheduled[end_time]': '1380','learn_duration':'240'}
}

class Domain:
    def __init__(self, domain, user):
        self.param = {'submit': '1', '_sand_ajax': '1', '_sand_platform': '3', '_sand_readmin': '1', '_sand_is_wan': 'false',
                      '_sand_ga_sessionToken': '', '_sand_ga_browserToken': '', '_sand_domain': domain, '_sand_masked': ''}
        self.user = self.get_token(user)

    def send(self, type, url, payload):
        url = SERVER + url
        payload.update(self.param)
        rq = requests.request(type, url=url, data=payload, headers=HEADER)
        return rq.json()

    def get_token(self, user):
        payload = {'lname': user, 'pass': PW}
        r = self.send('POST', '/user/login', payload)
        try:
            r = r['result']
            info = {'_sand_token': r['token'],
                    '_sand_uiid': r['iid'], '_sand_uid': r['id']}
            self.param.update(info)
            info.update({'code': user})
            return info
        except:
            return r['message']
    
    def add_session(self,course_iid,sesion):
        payload = {
            'name':sesion['name'],
            'scheduled[date_time]':sesion['date'],
            'enable_recording':'1',
            'location':'ilt_bbb',
            'type':'',
            'count':'1',
            'course_iid':course_iid
        }
        for x in range(len(sesion['teacher'])):
            payload.update({'scheduled[teacher_iids]['+str(x)+']':sesion['teacher'][x]})
        payload.update(RANGE_TIME[sesion['time']])
        r = self.send('POST','/session/new',payload)
        if r['success']:
            print(f"Đã tạo buổi học: {sesion['name']} > Ngày: {sesion['date']}")
        else:
            print(r)

    def detail(self,user_iid):
        payload ={
            'ntype': 'user',
            'editing_syllabus': '1',
            'iid': user_iid
        }
        r = self.send('POST', '/user/detail', payload)
        return r['result']

    def add_gv(self,iid_course,list_teacher, roles):
        payload = {'course_iid': iid_course}
        for i in range(len(list_teacher)):
            iid = list_teacher[i]
            teacher = self.detail(iid)
            temp = {
                    'o['+str(i)+'][name]': teacher['name'],
                    'o['+str(i)+'][iid]': teacher['iid'],
                    'o['+str(i)+'][id]': teacher['id']
            }
            for j in range(len(roles)):
                temp.update({'o['+str(i)+'][roles]['+str(j)+']': roles[j]['value']})
            payload.update(temp)

        r = self.send('POST','/course/staff/add-staff',payload)

    def get_roles(self, iid_course):
        payload = {
            'applied_target_iid': iid_course,
            'type': 'course'
        }
        r = self.send('POST', '/abac-role/api/get-role-options', payload)
        return r['result']