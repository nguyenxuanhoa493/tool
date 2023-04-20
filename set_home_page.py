import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import user

school = info.Domain('potado', 'patado')

list_teacher = user.get_teacher(school)

for teacher in list_teacher:
    user.set_home_page(school, teacher, 'teacher')