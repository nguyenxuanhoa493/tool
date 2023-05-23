def add_surveys_to_applied_item(self, item_iids, survey_iid):
    
    payload ={
        'applied_position': 'end',
        'survey_iids[0]': survey_iid,
        'item_iids[0]': item_iids,
        'type': 'course',
        '_sand_step': 'add_surveys_to_applied_item',
        'apply_for_all_session': 0
    }
    r = self.send('POST', '/survey/api/add-applied-items', payload)
    print(r)
