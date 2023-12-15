from pywinauto import Application
from pywinauto.keyboard import send_keys
import time
import pytest



class TestCalculatorRev:

    @pytest.fixture(name='opencalculator')
    def open_calc(self):
        self.app = Application(backend='uia').start("calc.exe")
        time.sleep(3)
        self.dlg = self.app.connect(title='Calculator')
        yield
        self.dlg.top_window().child_window(title="Close Calculator", control_type="Button").click()


    # 1. test_mode_change: Changes the mode of the calculator back to Standard
    def test_mode_change(self, opencalculator):
        self.dlg.top_window().child_window(title='Open Navigation').click()
        self.dlg.top_window().child_window(auto_id='Standard').click_input()
        assert self.dlg.top_window().child_window(auto_id="Header").texts() == ['Standard']



class TestNotepadRev:

    @pytest.fixture(name="opennotepad")
    def openNotepad(self):
        self.app = Application(backend='uia').start('notepad.exe')
        time.sleep(2)
        self.dlg = self.app.connect(title_re=".*Notepad.*")
        yield
        print("\nNotepad Running in Background")


    @pytest.fixture(name="conclosenotepad")
    def concloseNotepad(self):
        self.app = Application(backend='uia').connect(title_re=".*Notepad.*")
        self.topdlg = self.app
        yield
        time.sleep(2)
        print("\nClosed Notepad")
        self.topdlg.top_window().child_window(title='Close').click()

    # 2. remove * and x in replace window
    def test_replace(self, opennotepad):
        self.dlg.top_window().child_window(title="Edit", control_type="MenuItem").select()
        self.dlg.top_window().child_window(title="Replace...	Ctrl+H", auto_id="23",
                                              control_type="MenuItem").select()
        self.dlg.top_window().child_window(title="Find what:", control_type="Edit").double_click_input()
        send_keys("{BKSP}")
        self.dlg.top_window().child_window(title="Replace with:", control_type="Edit").double_click_input()
        send_keys("{BKSP}")
        self.dlg.top_window().child_window(title="Replace", control_type="Window").child_window(title="Close").click()

    # 3. test_font: Changes the font of the text back to default
    def test_font(self, conclosenotepad):
        self.topdlg.top_window().child_window(title="Format").select()
        self.topdlg.top_window().child_window(title="Font...", auto_id="33", control_type="MenuItem").select()
        self.topdlg.top_window().child_window(title='Font:', control_type='Edit').type_keys("Ar")
        self.topdlg.top_window().child_window(title="Arial", control_type="ListItem").double_click_input()
        self.topdlg.top_window().child_window(title='Font style:', control_type='Edit').type_keys("Reg")
        self.topdlg.top_window().child_window(title="Regular", control_type="ListItem").double_click_input()
        self.topdlg.top_window().child_window(title='Size:', control_type='Edit').type_keys("10")
        self.topdlg.top_window().child_window(title="OK", control_type="Button").click()

# 4. test_del pdf:  It opens the File Explorer and deletes the DemoFolder
def test_del_pdf():
    app = Application(backend='uia').start("explorer")
    time.sleep(3)
    dlg = app.connect(title="File Explorer")
    dlg.window(title="File Explorer").child_window(title="Downloads (pinned)").click_input()
    dlg.window(title="Downloads").child_window(title="DemoFolder").click_input()
    send_keys("+{DELETE}")
    send_keys("{ENTER}")
    dlg.window(title="Downloads").child_window(title="Close").click_input()
