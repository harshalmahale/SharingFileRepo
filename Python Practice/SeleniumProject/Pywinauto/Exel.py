from pywinauto import Application

# Launch Microsoft Excel
app = Application().start("excel.exe")

# Connect to the running instance of Excel
excel = app.connect(title="Microsoft Excel")
