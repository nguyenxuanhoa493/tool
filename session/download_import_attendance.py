import webbrowser
import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import course
school = info.Domain('bvl', 'bvl')
iid_course = 6630987
url_import = course.download_import_attendance(school, iid_course)
webbrowser.open(url_import)