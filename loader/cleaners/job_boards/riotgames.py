from cleaners.job_boards.job_boards_base_cleaner import JobBoardsBaseCleaner

class RiotgamesJobCleaner(JobBoardsBaseCleaner):
    def get_clean_data(self):
        return self.data

    def clean(self):
        self.clean_data()
        self.organize_data()
        self.data_to_list_of_tuples()

    def clean_data(self):
        def get_company_id_from_link(link):
            return link.split('/')[-1]

        for ind, a in enumerate(self.data):
            self.data[ind]['company'] = 'riotgames'
            self.data[ind]['company_id'] = get_company_id_from_link(a['link'])


