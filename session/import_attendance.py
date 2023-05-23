import webbrowser
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))

import info
import course
import session
school = info.Domain('bvl', 'bvl')

def download_import_attendance():
    url_import = course.download_import_attendance(school, iid_course)
    webbrowser.open(url_import)

def update_attendance(file_path):
    url_file = info.upload(school,file_path)
    id_file = session.import_file(school, url_file, iid_course)
    session.import_attendance(school, iid_course, id_file)

iid_course = 9328274
# download_import_attendance()

update_attendance(r"C:\Users\Moderator\Documents\9328274.xlsx")