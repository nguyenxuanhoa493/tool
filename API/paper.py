def new(self, count, random, shuffle, round):
    payload = {
        'count': count,
        'randomize_answers_in_question': random,
        'shuffle_questions': shuffle,
        'exam_round_iid': round['iid'],
        'syllabus_iid': round['syllabus']
    }
    r = self.send('POST', '/paper/new', payload)
    if r['success']:
        print(f"Đã tạo {count} đề trộn")

def search(self,round,page=1,items_per_page=-1):
    payload ={
        'syllabus_iid': round['syllabus'],
        'page': page,
        'items_per_page': items_per_page
    }

    r = self.send('POST', '/paper/index/search', payload)
    if r['objects']['count']:
        return r['result']
    else:
        return False
    
def unset(self,pape_iid):
    payload = {
        'id': pape_iid,
        '_sand_step': 'status',
        'type': 'undefined',
        'status': 'queued'
    }

    r = self.send('POST', '/paper/update', payload)
    if r['success']:
        print(f"Hủy duyệt {pape_iid}")
    else:
        print(r)