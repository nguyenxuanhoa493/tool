import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))
import info
import course
from print_json import PJ


courses = [9382045, 9382039, 9382034, 9382028,
           9382018, 9382012, 9382005, 9358486]
school = info.Domain('potado', 'patado')

course1 = course.Course(school, 9382045)

for s in course1.session:
    print(f"{s['name']} - {s['status']}")
