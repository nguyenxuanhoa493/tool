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