from pywinauto.application import Application
import time
app = Application(backend="uia").start("notepad.exe")
time.sleep(3)

app.UntitledNotepad.type_keys("%FX")