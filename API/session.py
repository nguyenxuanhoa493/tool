
def attendance_one_user(self, iid_course, session, user):
    payload = {'type': 'session_for_user',
               'course_iid': iid_course,
               'ntype': 'session',
               'iid': session['iid'],
               'id': session['id'],
               '_sand_step': 'attendance',
               'attendance[status]': '1',
               'attendance[user_iid]': user['iid']}
    r = self.send('POST', '/session/update', payload)
    if r['success']:
        print(session['name'], ' > ', user['name'])
    else:
        print('lỗi')


def import_file(self, url, iid_course):
    payload = {
        'import_file': url,
        'course_iid': iid_course
    }
    r = self.send('POST', '/attendance/import/import', payload)
    id_import = r['result']['import_id']
    print(f">>> Id import: {id_import}")
    return id_import


def import_attendance(self, iid_course, id_file):
    payload = {
        'importId': id_file,
        'course_iid': iid_course
    }
    r = self.send('POST', '/attendance/import/process', payload)
    print(r['message'])
