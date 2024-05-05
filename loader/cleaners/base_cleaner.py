class BaseCleaner():
    def __init__(self, raw_data) -> None:
        self.data = raw_data
        self.clean()

    def clean(self):
        print('base cleaner. if you see this, probably somethings wrong')
