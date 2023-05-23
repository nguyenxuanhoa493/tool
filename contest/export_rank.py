import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))
import info
import contest
import pandas as pd

school = info.Domain('bvl','bvl')
iid_contest = 6318981

exam_rounds =  contest.exam_rounds(school, iid_contest)

for round in exam_rounds:
    round_name = round['name'].replace('/','-')
    data = contest.rank(school, round['iid'])
    temp=[]
    for item in data:
        temp.append({
            'org':item['__expand']['orgs'][0]['short_name'],
            'code': item['__expand']['user']['code'],
            'name': item['__expand']['user']['name'],
            'take_count': item['take_count'],
            'total_score': item['total_score'],
            'average_score': item['average_score'],
            'total_spent_time': item['total_spent_time'],
            'average_spent_time': item['average_spent_time']

        })
    df = pd.DataFrame(temp)
    print(df)
    df.to_excel('./contest/'+round_name+'.xlsx', sheet_name= 'Bảng xếp hạng', index=False)


