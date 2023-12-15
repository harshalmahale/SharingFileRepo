from pywinauto import Application
import time

# Launch Microsoft Word
app = Application(backend="uia").start(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.exe")

