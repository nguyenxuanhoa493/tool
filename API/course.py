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

    