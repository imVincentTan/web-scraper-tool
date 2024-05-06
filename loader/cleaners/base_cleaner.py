class BaseCleaner():
    def __init__(self, raw_data) -> None:
        self.data = raw_data
        self.columns = []
        self.clean()

    def clean(self):
        print('base cleaner. if you see this, probably somethings wrong')

    def get_clean_data(self):
        return self.data
    
    def data_to_list_of_tuples(self):
        self.data = [[row[col] for col in self.columns] for row in self.data]