import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import user

school = info.Domain('tdu2', 'tdu2')
list_user = [637615,637614,637613,637612,637611,637610,637609,637608,637607,637606,637605,637604,637603]
for u in list_user:
    user.add_roles(school, u)