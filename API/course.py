class Course:
    def __init__(self, school, iid_course) -> None:
        self.users = list_user(school, iid_course)
        self.sessions = list_sesion(school, iid_course)


def list_user(self, iid_course):
    payload = {'item_iid': iid_course, 'items_per_page': '-1', 'page': '1'}
    r = self.send('POST', '/course/member/search', payload)
    list_user = []
    for u in r['result']:
        list_user.append(
            {
                'iid': u['user']['iid'],
                'code': u['user']['code'],
                'name': u['user']['name']
            })
    return list_user


def list_sesion(self, iid_course):
    # Chỉ get những buổi đã kết thúc
    payload = {'course_iid': iid_course, 'items_per_page': '-1',
               'page': '1', 'session_status[]': '1'}
    r = self.send('POST', '/session/search', payload)
    return r['result']


def download_import_attendance(self, iid_course):
    payload = {
        'type': 'attendance',
        'template': 'import_attendance',
        'course_iid': iid_course
    }
    r = self.send('POST', '/import/data/download-template-to-import', payload)
    return r['objects']['url']


def get_roles(self, iid_course):
    payload = {
        'applied_target_iid': iid_course,
        'type': 'course'
    }
    r = self.send('POST', '/abac-role/api/get-role-options', payload)
    return r['result']

def learn_video(self, iid_course, iid_video):
    payload = {'progress[0][tco_iid]': iid_video,
                'progress[0][p]': '100',
                'progress[0][pd][n]': '10',
                'progress[0][pd][i][0]': '0',
                'progress[0][pd][i][1]': '1',
                'progress[0][pd][i][2]': '2',
                'progress[0][pd][i][3]': '3',
                'progress[0][pd][i][4]': '4',
                'progress[0][pd][i][5]': '5',
                'progress[0][pd][i][6]': '6',
                'progress[0][pd][i][7]': '7',
                'progress[0][pd][i][8]': '8',
                'progress[0][pd][i][9]': '9',
                'progress[0][time_spent]': '300',
                'ciid': iid_course}
    r = self.send('POST', '/trckr2/save', payload)
    print(r)

def learn_pdf(self, iid_course, iid_pdf):
    payload = {'progress[0][tco_iid]': iid_pdf,
                'progress[0][p]': '100',
                'progress[0][time_spent]': '300',
                'ciid': iid_course}
    r = self.send('POST', '/trckr2/save', payload)

def get_syllabus_of_course(self, iid_course):
    payload = {'ntype': 'course', 'iid': iid_course}
    r = self.send('POST', '/api/v2/syllabus/get', payload)
    return r['result']['credit_syllabus']

def get_content_syllabus(self, iid_syllabus):
    payload = {'ntype': 'syllabus', 'iid': iid_syllabus, 'depth': '-1'}
    r = self.send('POST', '/api/v2/syllabus/get', payload)
    return r['result']['children']