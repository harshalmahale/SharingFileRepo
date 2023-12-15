from pywinauto import Application
from pywinauto.keyboard import send_keys
import time

# Open Calculator in Windows 10

app = Application(backend='uia').connect(title_re=".*Calculator")
dlg = app[u'Calculator']

time.sleep(2)

all_expression = []
repeat = 'y'
dlg['OpenNavigation0'].click()
time.sleep(1)
dlg['Scientific'].select()

while(repeat == 'y' or repeat=='Y'):
    exp = input("Enter expression:")          # format is 10-4/2
    dlg['openParenthesisButton'].click()
    dlg.type_keys(exp)
    time.sleep(2)
    dlg.type_keys('=')
    txt = dlg.Static3.texts()                # Get calculation result ['Display is 9']
    print(txt)
    txt = txt[0].split(' ')[2]               # Get only the numeric value    9
    ans = exp +"="+ txt
    all_expression.append(ans)
    repeat = input("Do you want to try more Expressions(y/n):")

app2 = Application(backend='uia').start("notepad.exe")      # Open Notepad from Windows 10

time.sleep(2)

for i in all_expression:
    time.sleep(1)
    app2.Untitled.edit.type_keys(i)                   #Display in Notepad
    send_keys('{ENTER}')


