from datetime import datetime
from cleaners.job_boards.job_boards_base_cleaner import JobBoardsBaseCleaner

class AmazonJobCleaner(JobBoardsBaseCleaner):
    def clean(self):
        self.clean_data()
        self.organize_data()
        self.data_to_list_of_tuples()

    def clean_data(self):
        def get_company_id_from_link(link):
            retval = ''
            link_split = link.split('/')
            try:
                id_index = link_split.index('jobs') + 1
                retval = link_split[id_index]
            except:
                retval = None
            return retval
        
        def clean_date(date):
            raw_date = date.split(':')[1].split('/')
            return datetime(int(raw_date[2]), int(raw_date[0]), int(raw_date[1]))

        for ind, a in enumerate(self.data):
            self.data[ind]['company'] = 'amazon'
            self.data[ind]['company_id'] = get_company_id_from_link(a['link'])
            self.data[ind]['posting_date'] = None
            self.data[ind]['last_updated'] = clean_date(a['last_updated'])

    def organize_data(self):
        def move_extra_columns_to_details_json(raw):
            details = {}
            for key in raw:
                if not key in self.columns:
                    details[key] = details[key]
                    del raw[key]
            if details:
                raw['details'] = details
            else:
                raw['details'] = None
            return raw
        
        self.data = [move_extra_columns_to_details_json(a) for a in self.data]

    def data_to_list_of_tuples(self):
        self.data = [[row[col] for col in self.columns] for row in self.data]
