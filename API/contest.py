def mark_take(self, iid_take):
    payload = {'id': iid_take}
    r = self.send('POST', '/take/api/mark-one-take', payload)
    if r['success']:
        print(iid_take + ' > Done')
    else:
        print(iid_take + ' > Lỗi')

def get_info(self,contest_iid):
    payload = {
        'ntype': 'contest',
        'depth': 1,
        'editing_syllabus': 1,
        'iid': contest_iid
    }
    r = self.send('POST', '/contest/setup/fetch-node', payload)
    return r['result']

def exam_rounds(self, contest_iid):
    payload = {
        'ntype': 'exam_round',
        'contest_iid': contest_iid
    }
    r = self.send('POST', '/exam-round/search', payload)
    return r['result']

def take_of_user(self,contest_iid,iid_user):
    payload = {
        'userIid': iid_user,
        'items_per_page': '-1',
        'contest_iid': contest_iid
    }
    
    r = self.send('POST', '/contest/api/get-user-taken-contests-results', payload)
    return r['result']

class contest: 
    def __init__(self,school,contest_iid):
        self.info = get_info(school, contest_iid)
        self.exam_rounds = exam_rounds(school,contest_iid)


def rank(self,exam_round_iid):
    payload = {
        'criteria':'take_count',
        'exam_round_iid':exam_round_iid,
        'items_per_page':'1000000',
        'page':1,
    }
    r = self.send('POST', '/contest/score/rank', payload)
    return r['result']