class Syllabus:
    def __init__(self,school,iid_syllabus) -> None:
        self.detail = detail(school,iid_syllabus)


def add_video_youtube(self, iid_sco, video):
    payload = {
        'type': 'video',
        'editingItemIid': iid_sco,
        'name': video['name'],
        'youtube[id]': video['id'],
        'youtube[max]': '00:00',
        'youtube[et]': '00:00',
        'youtube[st]': '00:00',
    }
    r = self.send('POST', '/video/new', payload)
    return r['result']

def detail(self, iid_syllabus):
    payload = {
    'ntype': 'syllabus',
    'depth': '-1',
    'is_preview': 1,
    'editing_syllabus': 2,
    'iid': iid_syllabus
    }
    r = self.send('POST', '/api/v2/syllabus/get', payload)

    print(f"Đã load thông tin syllabus {iid_syllabus} - {r['result']['name']}")
    return r['result']

def update(self, iid_syllabus, content):
    syllabus = detail(self, iid_syllabus)
    payload = {
        'id': syllabus['id'],
        'iid': syllabus['iid'],
        'ntype': 'syllabus',
        'type': 'credit',
        '_sand_step': 'children'
    }
    for i in range(len(content)):
        temp = {
            'children['+str(i)+'][id]': content[i]['id'],
            'children['+str(i)+'][iid]': content[i]['iid'],
            'children['+str(i)+'][ntype]': 'video',
            'children['+str(i)+'][pid]': iid_syllabus,
            'children['+str(i)+'][name]': content[i]['name'],
            'children['+str(i)+'][type]': 'video'
        }
        payload.update(temp)
    r = self.send('POST', '/syllabus/update', payload)
    print(r['message'])


def new(self,name,code,academic_categories,iid_org):
    payload ={
        'academic_categories[0]': academic_categories,
        'organizations[0]': iid_org,
        'student_have_to_join_session_to_download_materials': 0,
        'allow_teacher_add_new_session': 1,
        'name': name,
        'code': code,
        'max_depth': 2,
        'type': 'credit'
    }
    r = self.send('POST', '/syllabus/new', payload)
    print(r)
    

def add_role(self, iid_syllabus, user, role):
    payload = {
        'sid': iid_syllabus,
        'roleAppliedTargetIid': iid_syllabus,
        'type': 'syllabus',
        'elementSearchProps[_sand_step]': 'staff',
        'elementSearchProps[item_iid]': iid_syllabus,
        'elementSearchProps[type]': 'syllabus',
        '_sand_step': 'resource_staff'
    }
    for i in range(len(user)):
        temp = {
            'o['+str(i)+'][name]': user[i]['name'],
            'o['+str(i)+'][avatar]':'',
            'o['+str(i)+'][iid]': user[i]['iid'],
            'o['+str(i)+'][id]': user[i]['id'],
            'o['+str(i)+'][roles][0]': role
        }
        payload.update(temp)
    r = self.send('POST', '/user-abac-role/update', payload)

def get_role(self,iid_syllabus):
    payload = {
        'applied_target_iid': iid_syllabus,
        'type': ''
    }
    r = self.send('POST', '/abac-role/api/get-role-options', payload)
    return r['result'][0]['value']

def new_role(self,iid_syllabus, role):
    payload  = {
        'abstractIids[0]': role,
        'type': 'syllabus',
        'applied_target_iid': iid_syllabus
    }

    r = self.send('POST', '/abac-role/new-from-abstract', payload)

def get_abstract_role(self, iid_syllabus):
    payload = {
        'type': 'syllabus',
        'sub_type': 'syllabus_normal',
        'applied_target_iid': iid_syllabus
    }
    r = self.send('POST', '/abac-role/api/get-abstract-roles-options-for-specific-role-type', payload)
    return r['result'][0]['iid']

