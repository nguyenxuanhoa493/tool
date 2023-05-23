from API import info
from API import user

school = info.Domain('potado', 'patado')

list_teacher = user.get_teacher(school)

for teacher in list_teacher:
    print(f"{teacher['code']} - {teacher['name']}")
    # user.set_home_page(school, teacher, 'teacher')
