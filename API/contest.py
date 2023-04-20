def mark_take(self, iid_take):
    payload = {'id': iid_take}
    r = self.send('POST', '/take/api/mark-one-take', payload)
    if r['success']:
        print(iid_take + ' > Done')
    else:
        print(iid_take + ' > Lỗi')

def get_info(self,iid_contest):
    payload = {
        'ntype': 'contest',
        'depth': 1,
        'editing_syllabus': 1,
        'iid': iid_contest
    }
    r = self.send('POST', '/contest/setup/fetch-node', payload)
    return r['result']

def exam_rounds(self, iid_contest):
    payload = {
        'ntype': 'exam_round',
        'contest_iid': iid_contest
    }
    print(payload)
    r = self.send('POST', '/exam-round/search', payload)
    return r['result']

def take_of_user(self,iid_contest,iid_user):
    payload = {
        'userIid': iid_user,
        'items_per_page': '-1',
        'contest_iid': iid_contest
    }
    
    r = self.send('POST', '/contest/api/get-user-taken-contests-results', payload)
    return r['result']

class contest: 
    def __init__(self,school,iid_contest):
        self.info = get_info(school, iid_contest)
        self.exam_rounds = exam_rounds(school,iid_contest)
