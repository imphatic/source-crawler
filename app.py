from tkinter import *
from styles import Styles
from listeners import Listeners

window = Tk()
window.title("Source Crawler")
window.configure(background="black")

listeners = Listeners()

Label(window, Styles('label', {'text': 'Web Address'})).grid(row=0, column=0, sticky=W)
entry_web_address = Entry(window, Styles('entry'))
entry_web_address.grid(row=1, column=0, sticky=W)

Label(window, Styles('label', {'text': 'Search Term'})).grid(row=2, column=0, sticky=W)
entry_search_term = Entry(window, Styles('entry'))
entry_search_term.grid(row=3, column=0, sticky=W)

Button(window, text="Start Search", width=15, command=lambda: listeners.button_start_search(address=entry_web_address, term=entry_search_term)).grid(row=4, column=0, sticky=W)


window.mainloop()
