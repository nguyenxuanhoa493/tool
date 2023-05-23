import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
from print_json import PJ
import syllabus
data =[
 {
   "name": "Định hướng nghề nghiệp",
   "code": 301001960,
   "cate": 7714989,
   "org": 7707412
 },
 {
   "name": "Ngôn ngữ học đối chiếu",
   "code": 301000347,
   "cate": 7714990,
   "org": 7707412
 },
 {
   "name": "Thực tế ngoài trường NNA",
   "code": 301001576,
   "cate": 7714991,
   "org": 7707412
 },
 {
   "name": "Tiếng Anh bán hàng",
   "code": 301001963,
   "cate": 7714992,
   "org": 7707412
 },
 {
   "name": "Tiếng Anh y khoa",
   "code": 301001962,
   "cate": 7714993,
   "org": 7707412
 },
 {
   "name": "Nghe nói 5",
   "code": 301000725,
   "cate": 7714994,
   "org": 7707412
 },
 {
   "name": "Khóa luận tốt nghiệp - NNA",
   "code": 301001577,
   "cate": 7714995,
   "org": 7707412
 },
 {
   "name": "Ngữ nghĩa học nâng cao",
   "code": 301000727,
   "cate": 7714996,
   "org": 7707412
 },
 {
   "name": "Thực tập tốt nghiệp - NNA",
   "code": 301000517,
   "cate": 7714997,
   "org": 7707412
 },
 {
   "name": "Tiểu luận tốt nghiệp - NNA",
   "code": 301002517,
   "cate": 7714998,
   "org": 7707412
 },
 {
   "name": "Chủ nghĩa xã hội - khoa học",
   "code": 301001826,
   "cate": 7714999,
   "org": 7714874
 },
 {
   "name": "Kinh tế chính trị Mác-Lênin",
   "code": 301001825,
   "cate": 7715000,
   "org": 7714874
 },
 {
   "name": "Lịch sử Đảng Cộng Sản Việt Nam",
   "code": 301001827,
   "cate": 7715001,
   "org": 7714874
 },
 {
   "name": "Pháp luật đại cương",
   "code": 301000667,
   "cate": 7715002,
   "org": 7714874
 },
 {
   "name": "Triết học Mác - Lênin",
   "code": 301001769,
   "cate": 7715003,
   "org": 7714874
 },
 {
   "name": "Tư tưởng Hồ Chí Minh",
   "code": 301000665,
   "cate": 7715004,
   "org": 7714874
 },
 {
   "name": "Tin học căn bản",
   "code": 301001673,
   "cate": 7715005,
   "org": 7715082
 },
 {
   "name": "Cơ sở văn hóa Việt Nam",
   "code": 301000060,
   "cate": 7715006,
   "org": 7714927
 },
 {
   "name": "Pháp văn 1",
   "code": 301002404,
   "cate": 7715007,
   "org": 7707412
 },
 {
   "name": "Pháp văn 2",
   "code": 301002480,
   "cate": 7715008,
   "org": 7707412
 },
 {
   "name": "Đọc 1",
   "code": 301000121,
   "cate": 7715009,
   "org": 7707412
 },
 {
   "name": "Nghe nói 1",
   "code": 301000328,
   "cate": 7715010,
   "org": 7707412
 },
 {
   "name": "Ngữ âm thực hành 1",
   "code": 301000350,
   "cate": 7715011,
   "org": 7707412
 },
 {
   "name": "Ngữ pháp 1",
   "code": 301000357,
   "cate": 7715012,
   "org": 7707412
 },
 {
   "name": "Viết 1",
   "code": 301002507,
   "cate": 7715013,
   "org": 7707412
 }
]
school = info.Domain('tdu2', '01068024')
for i in data:
    syllabus.new(school, i['name'], i['code'], i['cate'], i['org'])