# The below code is doing the following:
# 1. Connect to Calculator running in background
# 2. Switch Scientific Calculator
# 3. Take input from user
# 4. Calculate the expression
# 5. Open Notepad
# 6. Display the expression and result in Notepad
# 7. Replace all * with x
# 8. Print the Notepad content
# 9. Save the Notepad content as PDF
from pywinauto import Application, keyboard
from pywinauto.keyboard import send_keys
import pywinauto
import time

# Team 1 --------------------------------------------------------------------------------------------------------------------
# Connect to Calculator in Windows 10

def strChange(str2):
    finalString = ''
    for i in str2:
        if i.isdigit():
            finalString += i
        else:
            finalString += '{' + i + '}'
    return finalString

app = Application(backend='uia').connect(title='Calculator')
dlg = app['Calculator']

time.sleep(2)

all_expression = []
repeat = 'y'
dlg['Open Navigation'].click()
time.sleep(1)

# to select Scientific Mode
dlg['Scientific'].select()

while (repeat == 'y' or repeat == 'Y'):
    exp = input("Enter expression:")  # format is 10-4/2
    exp1 = strChange(exp)
    dlg['openParenthesisButton'].click()
    dlg.type_keys(exp1)
    time.sleep(2)
    dlg.type_keys('=')
    txt = dlg.Static3.texts()  # Get calculation result ['Display is 9']
    print(txt)
    txt = txt[0].split(' ')[2]  # Get only the numeric value  9
    ans = exp1 + "=" + txt
    all_expression.append(ans)
    repeat = input("Do you want to try more Expressions(y/n):")

app2 = Application(backend='uia').start("notepad.exe")  # Open Notepad from Windows 10

time.sleep(2)

for i in all_expression:
    time.sleep(1)
    app2.Untitled.edit.type_keys(i)  # Display in Notepad
    send_keys('{ENTER}', with_spaces=True)

# team 2 ---------------------------------------------------------------------------------------------------------------------------------------
app3 = Application(backend="uia").connect(title_re=".*Notepad.*")
dlg_notepad_ops = app3.top_window()

edit1 = dlg_notepad_ops.child_window(title='Edit', control_type="MenuItem").click_input()

dlg_notepad_ops.menu_select("View -> Status Bar")
time.sleep(3)

dlg_notepad_ops.menu_select("Edit -> Replace")
time.sleep(3)

find_edit = dlg_notepad_ops.child_window(title="Find what:", control_type="Edit").type_keys('*')
replace_edit = dlg_notepad_ops.child_window(title="Replace with:", control_type="Edit")
replace_edit.double_click_input()
replace_edit.type_keys('x')

dlg_notepad_ops.child_window(title="Replace All", control_type="Button").click()
dlg_notepad_ops.child_window(title="Cancel", control_type="Button").click()

main_dlg = app3.top_window()
main_dlg.wait('visible')

font_menu = main_dlg.menu_select('Format->Font...p')
font_item = main_dlg.window(title='Font:', control_type='Edit').type_keys("Elephant")
font_style = main_dlg.window(title='Font style:', control_type='Edit').type_keys("Bold")
font_size = main_dlg.window(title='Size:', control_type='Edit').type_keys("25")
ok_button = main_dlg.window(title='OK', control_type="Button").click()

keyboard.send_keys('^p')

time.sleep(3)
print_win_handle = pywinauto.findwindows.find_windows(title="Print")[0]
print_win = app2.window(handle=print_win_handle)

print_win[u'Folder View']['Microsoft Print to PDF'].select()
print_win["print"].click_input()

time.sleep(2)

save_win_handle = pywinauto.findwindows.find_windows(title=u'Save Print Output As')[0]
save_win = app2.window(handle=save_win_handle)
save_win.type_keys("pywinauto")
time.sleep(1)
save_win['This PC'].select()
time.sleep(1)
save_win['Downloads'].click_input()
time.sleep(1)
save_win[u'New folder'].click_input()
time.sleep(1)
save_win.type_keys("Example{ENTER}{ENTER}")
time.sleep(1)
save_win["Save"].click_input()
