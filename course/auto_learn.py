import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))
from API import info
from API.course import Course, learn_video, learn_pdf

school = info.Domain('khachhang', 'khachhang')
iid_course =  9496918  
data = Course(school,iid_course)
# list_user=""""""
# list_user.replace('\n', ' ')
# list_user = list_user.split(' ')
# print(list_user)
content = data.syllabus.detail['children']
def learn(content):
    for item in content:
        tpl_type = item.get('tpl_type', None)
        item_type = item.get('type', None)
        item_ntype = item.get('ntype', None)
        
        if tpl_type== 'standard':
            learn(item['children'])
            
        elif item_type == 'video':
            print('[Video]: ' ,item['name'],'-',item['iid'])
            learn_video(school,iid_course, item['iid'])

        elif item_ntype == 'exercise':
            print(f"[{item_ntype}] - {item['name']} - {item['iid']}")

        else:
            print('[',item_type,']:', item['name'],'-',item['iid'])
            learn_pdf(school,iid_course, item['iid'])

for user in data.users:
    print('user: ', user['name'])
    info.login(school, user['code'],'vieted@2022@123')
    learn(content)

