def new(self, name, code):
    payload = {
        'type': 'academic',
        'name': name,
        'code': code,
        'status': 'init'
    }
    r = self.send('POST', '/category/index/new', payload)
    return r['result']


