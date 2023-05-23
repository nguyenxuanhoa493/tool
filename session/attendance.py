import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
from API import info
from API.course import Course
from API.session import attendance_one_user 

school = info.Domain('bvl','bvl')

iid_course = 9354829
data = Course(school, iid_course)
checked="""sp-vieted"""
checked = checked.split('\n')
print(checked)

for s in data.session:
    for u in data.users:
        # nếu ds user rỗng hoặc có và u.code trong list đó thì đc điểm danh
        if (checked[0]=="") or (checked[0]!="" and (u['code'] in checked)):
            attendance_one_user(school, iid_course, s, u)

