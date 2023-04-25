import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')


import uni
school = uni.Domain('hth', 'hth')
course_iid = 2008158
teacher_master = [267517]


data = [{'name':'CĐ 2. Thảo luận','date':'2023-4-21','time':'Tối','teacher':[267497]},
{'name':'CĐ 3: Công vụ, công chức','date':'2023-4-22','time':'Tối','teacher':[267499]},
{'name':'CĐ 3. Thảo luận','date':'2023-4-23','time':'Tối','teacher':[267499]},]
for session in data:
    session['teacher']+=teacher_master
    school.add_session(course_iid,session)
list_teacher = teacher_master
for session in data:
    list_teacher += session['teacher']

roles = school.get_roles(course_iid)
#gán list gv có tất cả các quyền vào khóa học
school.add_gv(course_iid, list(set(list_teacher)), roles)
