def new(self, name, code):
    payload = {
        'type': 'academic',
        'name': name,
        'code': code,
        'status': 'init'
    }
    r = self.send('POST', '/category/index/new', payload)
    try:
        r= r['result']
        approved(self,r['id'])
        print(f"{name} - {code} - {r['iid']}")
        return r['result']
    except:
        pass

def approved(self,id_academic):
    payload ={
        'id': id_academic,
        '_sand_step': 'status',
        'type': 'academic',
        'status': 'approved',
    }
    r = self.send('POST', '/category/update', payload)



