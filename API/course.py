from .syllabus import Syllabus

class Course:
    def __init__(self, school, iid_course) -> None:
        self.detail = detail(school,iid_course)
        self.users =  list_user(school,iid_course)
        self.session = list_session(school,iid_course)
        self.syllabus = Syllabus(school,self.detail['syllabus'])

def detail(self,iid):
    payload = {
        'ntype': 'course',
        'depth': 2,
        'is_preview': 'false',
        'editing_syllabus': 2,
        'iid': iid
    }
    r = self.send('POST', '/api/v2/syllabus/get', payload)
    print(f"Course: {iid} - {r['result']['name']}")
    return r['result']


def list_user(self, iid_course):
    payload = {'item_iid': iid_course, 'items_per_page': '-1', 'page': '1'}
    r = self.send('POST', '/course/member/search', payload)

    list_user = []
    try:
        for u in r['result']:
            list_user.append(
                {
                    'iid': u['user']['iid'],
                    'code': u['user']['code'],
                    'name': u['user']['name']
                })
        print(f"Đã load thông tin của {len(list_user)} học viên")
        return list_user
    except:
        print('Course chưa có học viên')
        return []

def list_session(self, iid_course):
    payload = {
        'session_status[]': 2,
        'session_status[]': 3,
        'session_status[]': 1,
        '_sand_expand[]': 'scheduled',
        '_sand_expand[]': 'survey',
        'is_teacher': 0,
        'enrolment_plan_statuses[]': 'executed',
        'get_attendance_status': 1,
        'course_iid': iid_course,
        'submit': 1,
        'page': 1,
        'items_per_page': -1,
        }
    r = self.send('POST', '/session/search', payload)
    try:
        print(f"Đã load thông tin {r['count']} buổi học")
        return r['result']
    except:
        print('Course chưa tạo buổi học')
        return []


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


def learn_pdf(self, iid_course, iid_pdf):
    payload = {'progress[0][tco_iid]': iid_pdf,
                'progress[0][p]': '100',
                'progress[0][time_spent]': '300',
                'ciid': iid_course}
    r = self.send('POST', '/trckr2/save', payload)



def list_teacher(self,iid_course):
    payload ={
        'resource_iid': iid_course,
        'applied_scope': 'course',
        '_sand_step': 'list_members'
    }
    r = self.send('POST', '/user/search', payload)
    try:
        return r['result']
    except:
        print('course không có GV')
        return False
    
if __name__ == '__main__':
    pass