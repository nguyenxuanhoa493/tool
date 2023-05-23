import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\Moderator\OneDrive\Tools\API')


import uni
school = uni.Domain('hth', 'hth')
course_iid = 2008185
teacher_master = [267518]


data = [{'name':'CĐ 9: Kỹ năng làm việc trong môi trường số','date':'2023-5-15','time':'Tối','teacher':[267506]},
{'name':'CĐ 9. Thảo luận','date':'2023-5-16','time':'Tối','teacher':[267506]},
{'name':'CĐ 6: Kỹ năng thuyết trình trong hoạt động công vụ','date':'2023-5-17','time':'Tối','teacher':[267500]},
{'name':'CĐ 6. Thảo luận','date':'2023-5-18','time':'Tối','teacher':[267500]},
{'name':'CĐ 2. Thảo luận','date':'2023-5-19','time':'Tối','teacher':[267499]},
{'name':'CĐ 8: Kỹ năng quản lý thời gian','date':'2023-5-20','time':'Tối','teacher':[267495]},
{'name':'CĐ 8. Thảo luận','date':'2023-5-21','time':'Tối','teacher':[267495]},]
for session in data:
    session['teacher']+=teacher_master
    school.add_session(course_iid,session)
list_teacher = teacher_master
for session in data:
    list_teacher += session['teacher']

roles = school.get_roles(course_iid)
#gán list gv có tất cả các quyền vào khóa học
school.add_gv(course_iid, list(set(list_teacher)), roles)
