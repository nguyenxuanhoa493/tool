
import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import category

data =[['Đọc 4',301000124],
['Ngữ âm thực hành 2',301000351],
['Ngữ âm thực hành 3',301000352],
['Viết 3',301000640],
['Dẫn luận văn chương',301000084],
['Viết 2',301000639],
['Kỹ năng làm P.R',301001977],
['Dẫn luận ngôn ngữ *',301000083],
['Lý thuyết dich',301000297],
['Nghe nói 4',301000331],
['Văn hóa các nước nói tiếng Anh',301001958],
['Tiếng Anh thương mại',301000480],
['Tiếng Anh marketing',301001965],
['Nghe nói 2',301000329],
['Nghe nói 3',301000330],
['Đọc 3',301000123],
['Ngữ pháp 2',301000358],
['Ngữ pháp 3',301000359],
['Ngữ pháp 4',301001956],
['Viết 4',301000641],
['Phương pháp nghiên cứu khoa học NNA*',301000427],
['Tiếng Anh truyền thông',301001961],
['Tiếng Anh du lịch',301000479],
['Đọc 2',301000122],
['Ngữ nghĩa học - Ngữ dụng học',301001959],
['Tiếng Anh thư tín văn phòng',301001964],
['Kỹ năng thuyết trình - Nói trước công chúng*',301001957],
['Tiếng Anh giao tiếp nâng cao',301001973],
['Âm vị học',301001594]]
school = info.Domain('tdu2', 'tdu2')
for item in data:
    category.new(school, item[0], item[1])