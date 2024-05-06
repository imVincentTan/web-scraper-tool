import json
from cleaners.base_cleaner import BaseCleaner

class JobBoardsBaseCleaner(BaseCleaner):
    def __init__(self, raw_data) -> None:
        self.data = raw_data
        self.columns = ['company', 'company_id', 'link', 'title', 'location', 'posting_date', 'last_updated', 'details']
        self.clean()

    def clean(self):
        print('job boards base cleaner. if you see this, probably somethings wrong')

    def organize_data(self):
        def move_extra_columns_to_details_json(raw):
            details = {}
            keys_to_delete = []
            for key in raw:
                if not key in self.columns:
                    details[key] = raw[key]
                    keys_to_delete.append(key)

            for key in keys_to_delete:
                del raw[key]

            if details:
                raw['details'] = json.dumps(details)
            else:
                raw['details'] = None
            return raw
        
        self.data = [move_extra_columns_to_details_json(a) for a in self.data]
