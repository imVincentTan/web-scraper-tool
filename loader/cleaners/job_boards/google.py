from datetime import datetime
from cleaners.job_boards.job_boards_base_cleaner import JobBoardsBaseCleaner

class GoogleJobCleaner(JobBoardsBaseCleaner):
    def get_clean_data(self):
        return self.data

    def clean(self):
        self.clean_data()
        self.organize_data()
        self.data_to_list_of_tuples()

    def clean_data(self):
        def get_company_id_from_link(link):
            retval = ''
            link_split = link.split('/')
            try:
                id_index = link_split.index('results') + 1
                retval = link_split[id_index].split('-')[0]
            except:
                retval = None
            return retval
        
        def clean_link(link):
            return link.split('?')[0]

        for ind, a in enumerate(self.data):
            self.data[ind]['company'] = 'google'
            self.data[ind]['link'] = clean_link(a['link'])
            self.data[ind]['company_id'] = get_company_id_from_link(a['link'])
