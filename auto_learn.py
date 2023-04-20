import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import user

school = info.Domain('nioeh', 'nioeh')
iid_course = 5280577

list_user="""0339171828 0836054888"""
LIST_VIDEO = []
LIST_PDF = []
print(len(LIST_VIDEO))

# iid_syllabus = school.get_syllabus_of_course(iid_course)
# print('iid_syllabus:', iid_syllabus)
# content = school.get_content_syllabus(iid_syllabus)
# print('Đã load content')
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
            school.learn_video(iid_course, item['iid'])
        elif item_type == 'exercise':
            pass
        else:
            print('[',item_type,']:', item['name'],'-',item['iid'])
            school.learn_pdf(iid_course, item['iid'])

# for user in list_user:
#     print('user: ', user)
#     school.get_token(user)
#     for v in LIST_VIDEO:
#         school.learn_video(iid_course, v)

