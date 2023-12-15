# TestCalculator:
#
# 1. test_mode_change: Changes the mode of the calculator to Scientific
#
# 2. test_check_output: Checks the output of the expression entered on the calculator
#
# 3. test_close_calculator: Closes the calculator
#
# TestNotepad:
#
# 1. test_notepad_write: Writes the text in the notepad
#
# 2. test_replace: Replaces the * with x
#
# 3. test_font: Changes the font of the text
#
# 4. test_print: Prints the text in the notepad
#
# 5. test_make_folder: Makes a folder in the downloads and saves the pdf in it
#
# 6. test_open_pdf: Opens file explorer and click on download folder then open Demo pdf file
#
# 7. test_remove_func_start:if the pdf is running it stays then Runs a revarsal file
\import os

from pywinauto import Application
from pywinauto.keyboard import send_keys
import time
import pytest

input_list = [
    '5+2/2-1',
    '2+5/2*1*1^2',
    '8-2+2',
    '5%2*2+1-22',
    '2*(3-(2^3)+102'
]
text_list = ["Hi,this is the demo using Pywinauto Library", "Expressions"]


class TestCalculator:

    @staticmethod
    def str_change(str1):
        final_string = ''
        for i in str1:
            if i.isdigit():
                final_string += i       # 5*2^2 -> 5{*}2{^}2
            else:
                final_string += '{' + i + '}'
        return final_string

    @pytest.fixture(name='opencalculator')
    def open_calc(self):
        self.app = Application(backend='uia').start("calc.exe")
        time.sleep(3)
        self.dlg = self.app.connect(title='Calculator')
        yield
     print('\nCalculator Running in Background')

    @pytest.fixture(name='connectcalculator')
    def connect_calc(self):
        self.app = Application(backend='uia').connect(title='Calculator')
        self.dlg = self.app
        yield
        print("\nConnected Calculator")

    # 1. test_mode_change: Changes the mode of the calculator to Scientific
    def test_mode_change(self, opencalculator):
        self.dlg.top_window().child_window(title='Open Navigation').click()
        self.dlg.top_window().child_window(auto_id='Scientific').click_input()
        assert self.dlg.top_window().child_window(auto_id="Header").texts() == ['Scientific']


    # 2. test_check_output: Checks the output of the expression entered on the calculator
    @pytest.mark.parametrize('exp', input_list)
    def test_check_output(self, connectcalculator, exp):
        exp_mod = self.str_change(exp)
        self.dlg.top_window()['openParenthesisButton'].click()
        self.dlg.top_window().type_keys(exp_mod)
        time.sleep(1)
        self.dlg.top_window().type_keys('=')
        display_txt = self.dlg.top_window().Static3.texts()
        print(display_txt)
        display_txt = display_txt[0].split(' ')[2]
        ans = exp_mod + "=" + display_txt
        text_list.append(ans)

    # 3. test_close_calculator: Closes the calculator
    def test_close_calculator(self, connectcalculator):
        self.dlg.top_window().child_window(title="Close Calculator", control_type="Button").click()


class TestNotepad:

    @pytest.fixture(name="opennotepad")
    def openNotepad(self):
        self.app = Application(backend='uia').start('notepad.exe')
        time.sleep(2)
        self.dlg = self.app.connect(title_re=".*Notepad.*")
        yield
        print("\nNotepad Running in Background")

    @pytest.fixture(name="connectnotepad")
    def connectNotepad(self):
        self.app = Application(backend='uia').connect(title_re=".*Notepad.*")
        self.topdlg = self.app
        yield
        print("\nStill Connected Notepad")

    @pytest.fixture(name="conclosenotepad")
    def concloseNotepad(self):
        self.app = Application(backend='uia').connect(title_re=".*Notepad.*")
        self.topdlg = self.app
        yield
        time.sleep(5)
        print("\nClosed Notepad")
        self.topdlg.top_window().child_window(title='Close').click()
        self.topdlg.top_window().child_window(title="Don't Save").click()

    # 1. test_notepad_write: Writes the text in the notepad
    def test_notepad_write(self, opennotepad):
        for i in text_list:
            self.dlg.top_window().type_keys(i, with_spaces=True)
            self.dlg.top_window().type_keys("{ENTER}")

    # 2. test_replace: Replaces the * with x
    def test_replace(self, connectnotepad):
        self.topdlg.top_window().child_window(title="Edit", control_type="MenuItem").select()
        self.topdlg.top_window().child_window(title="Replace...	Ctrl+H", auto_id="23",
                                              control_type="MenuItem").select()
        self.topdlg.top_window().child_window(title="Find what:", control_type="Edit").type_keys('*')
        self.topdlg.top_window().child_window(title="Replace with:", control_type="Edit").double_click_input()
        self.topdlg.top_window().child_window(title="Replace with:", control_type="Edit").type_keys('x')
        self.topdlg.top_window().child_window(title="Replace All", control_type="Button").click()
        self.topdlg.top_window().child_window(title="Cancel", control_type="Button").click()

    # 3. test_font: Changes the font of the text
    def test_font(self, connectnotepad):
        self.topdlg.top_window().child_window(title="Format").select()
        self.topdlg.top_window().child_window(title="Font...", auto_id="33", control_type="MenuItem").select()
        self.topdlg.top_window().child_window(title='Font:', control_type='Edit').type_keys("Cal")
        self.topdlg.top_window().child_window(title="Calibri", control_type="ListItem").double_click_input()
        self.topdlg.top_window().child_window(title='Font style:', control_type='Edit').type_keys("Bold")
        self.topdlg.top_window().child_window(title="Bold", control_type="ListItem").double_click_input()
        self.topdlg.top_window().child_window(title='Size:', control_type='Edit').type_keys("20")
        self.topdlg.top_window().child_window(title="OK", control_type="Button").click()

    # 4. test_print: Prints the text in the notepad
    def test_print(self, connectnotepad):
        self.topdlg.top_window().child_window(title="Text Editor").click_input()
        send_keys('^p')
        self.topdlg.top_window().child_window(title="Microsoft Print to PDF").select()
        self.topdlg.top_window().child_window(title="Print", control_type="Button").click()

    # 5. test_make_folder: Makes a folder in the downloads and saves the pdf in it
    def test_make_folder(self, conclosenotepad):
        self.topdlg.top_window().child_window(title="Downloads", control_type="TreeItem").click_input()
        self.topdlg.top_window().child_window(title="New folder", control_type="Button").click()
        time.sleep(1)
        send_keys("DemoFolder{ENTER}{ENTER}")
        self.topdlg.top_window().child_window(title="File name:", control_type="Edit").type_keys("DemoPdf.pdf")
        self.topdlg.top_window().child_window(title="Save", control_type="Button").click()
    # 6. test_open_pdf: Opens file explorer and click on download folder then open Demo pdf file
    def test_open_pdf(self):
        app = Application(backend='uia').start("explorer")
        time.sleep(3)
        dlg = app.connect(title="File Explorer")
        dlg.window(title="File Explorer").child_window(title="Downloads (pinned)").click_input()
        dlg.window(title="Downloads").child_window(title="DemoFolder").double_click_input()
        dlg.window(title="DemoFolder").child_window(title="DemoPdf.pdf").double_click_input()
        dlg.window(title="DemoFolder").child_window(title="Close").click()


def test_remove_func_start():
    time.sleep(5)
    while (True):
        try:
            app = Application(backend="uia").connect(title_re=".*DemoPdf.*")
            print("The pdf file is still visible")
        except Exception as e:
            print("Run destroy script")
            os.system("pytest DemoFileRev_test.py")
            break


