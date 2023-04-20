
def set_home_page(self, user, target):
    payload = {'iid': user['iid'],
                'id': user['id'],
                'default_home_page': target,
                '_sand_step': 'default_home_page'
                }
    r = self.send('POST', '/user/update', payload)
    print(f"{user['name']} > {r['message']}")

def detail(self,user_iid):
    payload ={
        'ntype': 'user',
        'editing_syllabus': '1',
        'iid': user_iid
    }
    r = self.send('POST', '/user/detail', payload)
    return r['result']


def get_teacher(self):
    payload= {
            'ntype': 'user',
            '_sand_step': 'students',
            'is_staff': 'true',
            'page': '1',
            'items_per_page': '-1'
    }
    r = self.send('POST', '/user/api/search', payload)
    return r['result']