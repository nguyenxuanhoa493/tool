import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import syllabus
import time

school = info.Domain('tdu2', 'tdu2')
data = [
{'name': 'Lê Thanh Trúc (  Ban Quản trị Thông tin & Truyền thông)',
'avatar': '',
'iid': '637598',
'id': '6447820b43a22d59e10e9b66'
},
{'name': 'Huỳnh Thanh Danh (  Phòng Đào tạo)',
'avatar': '',
'iid': '637600',
'id': '6447820e43a22d59e10e9b6e'
},
{'name': 'Âu Nguyễn Khôi Nguyên (  Phòng Đào tạo)',
'avatar': '',
'iid': '637601',
'id': '6447820f43a22d59e10e9b72'
},
{'name': 'Nguyễn Thị Bích Huyền (  Trung tâm NN-TH-CĐR và PTNNL)',
'avatar': '',
'iid': '637602',
'id': '6447821043a22d59e10e9b76'
}
]
list_syllabus = [7715191,7715170,7715177,7715156,7715163]
for iid_syllabus in list_syllabus:
    role = syllabus.get_abstract_role(school, iid_syllabus)
    syllabus.new_role(school, iid_syllabus, role)
    time.sleep(3)
    roled = syllabus.get_role(school, iid_syllabus)
    syllabus.add_role(school, iid_syllabus, data, roled)

