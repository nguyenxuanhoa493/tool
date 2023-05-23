
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

def add_roles(self,iid_user):
    payload = {
        'user_iid': iid_user,
        'applied_target_iid': 7707412,
        'fetchRoleOptionParams[type]': 'school',
        'fetchRoleOptionParams[applied_target_iid]': 7707412,
        'role_iids[0]': 7708702
    }
    r = self.send('POST', '/user-abac-role/update', payload)
    print(r)

def new_teacher(self,name,code):
    payload = {
        'name': name,
        'code': code,
        'mail': code+'@gmail.com',
        'pass': 123,
        'pass_retype': 123,
        '_sand_step':'staff',
        'user_organizations[0]': '2045706'
    }

    r = self.send('POST', '/user/new', payload)
    print(r)