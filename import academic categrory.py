
import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import category

data =[
 {
   "name": "Định hướng nghề nghiệp",
   "code": 301001960
 },
 {
   "name": "Ngôn ngữ học đối chiếu",
   "code": 301000347
 },
 {
   "name": "Thực tế ngoài trường NNA",
   "code": 301001576
 },
 {
   "name": "Tiếng Anh bán hàng",
   "code": 301001963
 },
 {
   "name": "Tiếng Anh y khoa",
   "code": 301001962
 },
 {
   "name": "Nghe nói 5",
   "code": 301000725
 },
 {
   "name": "Khóa luận tốt nghiệp - NNA",
   "code": 301001577
 },
 {
   "name": "Ngữ nghĩa học nâng cao",
   "code": 301000727
 },
 {
   "name": "Thực tập tốt nghiệp - NNA",
   "code": 301000517
 },
 {
   "name": "Tiểu luận tốt nghiệp - NNA",
   "code": 301002517
 },
 {
   "name": "Chủ nghĩa xã hội - khoa học",
   "code": 301001826
 },
 {
   "name": "Kinh tế chính trị Mác-Lênin",
   "code": 301001825
 },
 {
   "name": "Lịch sử Đảng Cộng Sản Việt Nam",
   "code": 301001827
 },
 {
   "name": "Pháp luật đại cương",
   "code": 301000667
 },
 {
   "name": "Triết học Mác - Lênin ",
   "code": 301001769
 },
 {
   "name": "Tư tưởng Hồ Chí Minh",
   "code": 301000665
 },
 {
   "name": "Tin học căn bản",
   "code": 301001673
 },
 {
   "name": "Cơ sở văn hóa Việt Nam",
   "code": 301000060
 },
 {
   "name": "Pháp văn 1",
   "code": 301002404
 },
 {
   "name": "Pháp văn 2",
   "code": 301002480
 },
 {
   "name": "Đọc 1",
   "code": 301000121
 },
 {
   "name": "Nghe nói 1",
   "code": 301000328
 },
 {
   "name": "Ngữ âm thực hành 1",
   "code": 301000350
 },
 {
   "name": "Ngữ pháp 1",
   "code": 301000357
 },
 {
   "name": "Viết 1",
   "code": 301002507
 }
]
school = info.Domain('tdu2', 'tdu2')
for item in data:
    category.new(school, item['name'], item['code'])