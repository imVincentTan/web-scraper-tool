from cleaners.job_boards.job_boards_base_cleaner import JobBoardsBaseCleaner

class EaJobCleaner(JobBoardsBaseCleaner):
    def clean(self):
        self.clean_data()
        self.organize_data()
        self.data_to_list_of_tuples()

    def clean_data(self):
        for ind, a in enumerate(self.data):
            self.data[ind]['company'] = 'ea'
