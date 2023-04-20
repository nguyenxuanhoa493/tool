import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import course
from session import attendance_one_user 

school = info.Domain('bvl','bvl')
iid_course = 6611032
checked=""""""
checked = checked.split('\n')
print(checked)
list_user = course.list_user(school,iid_course)
list_session = course.list_sesion(school,iid_course)

for s in list_session:
    for u in list_user:
        # nếu ds user rỗng hoặc có và u.code trong list đó thì đc điểm danh
        if (checked[0]=="") or (checked[0]!="" and (u['code'] in checked)):
            attendance_one_user(school, iid_course, s, u)

