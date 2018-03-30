class Listeners:
    def __int__(self):
        return None

    def button_start_search(self, **kwargs):
        print(kwargs['address'].get())
        print(kwargs['term'].get())
        return None
