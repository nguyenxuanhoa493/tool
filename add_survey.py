from API.survey import add_surveys_to_applied_item
from API import info

school = info.Domain('nevadaacademy', 'nevadaacademy')
list_survey = [9130936,9133875,9194060]
for survey in list_survey:
    add_surveys_to_applied_item(school, 9486720, survey)
