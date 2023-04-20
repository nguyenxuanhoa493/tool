import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import course

school = info.Domain('mtholding', 'TDMT')
iid_course = 4023763
course.learn_video(school, iid_course, 4310217)