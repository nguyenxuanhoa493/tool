import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import course

school = info.Domain('mtholding', 'TDMT')
iid_course = 4023773

list_user="""TDMT"""

iid_syllabus = course.get_syllabus_of_course(school,iid_course)
print('iid_syllabus:', iid_syllabus)
content = course.get_content_syllabus(school,iid_syllabus)
print('Đã load content')
list_user.replace('\n', ' ')
list_user = list_user.split(' ')
print(list_user)

def learn(content):
    for item in content:
        tpl_type = item.get('tpl_type', None)
        item_type = item.get('type', None)
        if tpl_type== 'standard':
            learn(item['children'])
        elif item_type == 'video':
            print('[Video]: ' ,item['name'],'-',item['iid'])
            course.learn_video(school,iid_course, item['iid'])
        elif item_type == 'exercise':
            pass
        else:
            print('[',item_type,']:', item['name'],'-',item['iid'])
            course.learn_pdf(school,iid_course, item['iid'])

for user in list_user:
    print('user: ', user)
    info.login(school, user)
    len(content)

