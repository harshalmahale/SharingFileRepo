"""
    It starts the application if it's not running, or connects to it if it is
    :return: The dialog object
"""

import time
import pytest
from pywinauto.application import Application

@pytest.fixture(name="start_app", scope="function")
def start_app_fixture():
    try:
        app = Application(backend="uia").connect(title="Wordpad Application")
        dlg = app
    except:
        app = Application(backend="uia").start(u"C:\Windows\WinSxS\wow64_microsoft-windows-wordpad_31bf3856ad364e35_10.0.22000.1_none_8e52c12ba60f5a2c")
        app.window(title_re="")





