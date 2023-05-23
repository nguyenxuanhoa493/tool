def search(self, key_conf):
    payload = { 'q': key_conf}
    r = self.send('POST', '/conf/api/search', payload)
    return r['result'][0]['content'][0]

def update(self, conf):
    key, content = conf
    print('get data key:', key)
    temp = search(self, key)

    payload = {
        'ntype': 'conf',
        'id': temp['id'],
        'type': temp['type']
    }
    payload.update({'content':content})
    r = self.send('POST', '/conf/update', payload)
    print(r)
