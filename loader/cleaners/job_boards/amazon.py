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

        for ind, a in enumerate(self.data):
            self.data[ind]['company'] = 'amazon'
            self.data[ind]['company_id'] = get_company_id_from_link(a['link'])
            self.data[ind]['posting_date'] = None
            self.data[ind]['last_updated'] = a['last_updated']
