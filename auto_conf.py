
import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')
from print_json import PJ
from conf import update
import info



school = info.Domain('khachhang', 'khachhang')
data = {
    'new_user_default_status': 'activated',
    'limit_file_size': 1000,
    'blog_theme':'viki',
    'question_exam_report_reason':{}
}
for item in data.items():
    update(school, item)