import webbrowser
import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import session 
school =info.Domain('bvl', 'bvl')
iid_course = 6630987
file_path = r'C:\Users\nguye\Downloads\ok.xlsx'

url_file = info.upload(school,file_path)
id_file = session.import_file(school, url_file, iid_course)
session.import_attendance(school, iid_course, id_file)