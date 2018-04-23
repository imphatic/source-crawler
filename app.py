import tkinter as tk
from styles import Styles


class App(tk.Frame):
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(parent)
        self.configure_window()
        # Place our App on the screen
        self.grid(pady=10, padx=20, sticky='EWNS')

        self.entry_web_address = self.add_web_address()
        self.entry_search_term = self.add_search_term()
        self.add_search_button()
        self.add_output_box()

    def configure_window(self):
        self.parent.geometry('800x600')
        self.parent.title("Source Crawler")
        self.parent.configure(background="black")
        self.configure(background="black")

    def add_web_address(self):
        label = tk.Label(self, Styles('label', {'text': 'Web Address'}))
        label.grid(row=0, column=0, sticky='W')
        entry_web_address = tk.Entry(self, Styles('entry'))
        entry_web_address.grid(row=1, column=0)
        return entry_web_address

    def add_search_term(self):
        label = tk.Label(self, Styles('label', {'text': 'Search Term'}))
        label.grid(row=0, column=2, sticky='W')
        entry_search_term = tk.Entry(self, Styles('entry'))
        entry_search_term.grid(row=1, column=2)
        return entry_search_term

    def add_search_button(self):
        button = tk.Button(self, text="Start Search", width=15, command=lambda: self.start_search())
        button.grid(row=1, column=3)
        return button

    def add_output_box(self):
        text = tk.Text(self, Styles('text'))
        text.grid(row=3, column=0, sticky='WS')
        return text

    def start_search(self):
        print(self.entry_web_address.get())
        print(self.entry_search_term.get())
        return None


# An empty root widget to build our application from
root = tk.Tk()
# Create our app and attach it to the root
app = App(parent=root)
# Run the app
app.mainloop()
