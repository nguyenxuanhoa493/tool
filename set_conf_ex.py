import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import syllabus
from print_json import PJ
school = info.Domain('khl', 'khl')
iid_syllabus = 7740108
PJ(syllabus.detail(school, iid_syllabus))