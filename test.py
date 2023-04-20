import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
school = info.Domain('bvl', 'bvl')
iid_course = 123
file_path = r'C:\Users\nguye\OneDrive\Tools\test.py'
url_file = info.upload(school,file_path)
