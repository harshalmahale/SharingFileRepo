from pywinauto.application import Application
import time
import pywinauto.keyboard as keyboard
import pywinauto.mouse as mouse

keyboard.send_keys('{LWIN}')
keyboard.send_keys('Run')
keyboard.send_keys('{ENTER}')
time.sleep(3)

app = Application(backend='uia')
time.sleep(3)
app.connect(title="Run")
run_app = app.Run

run_app.Combobox.Edit. type_keys("mswindowsmusic:")
time.sleep(1)
run_app.OKButton.click()
time.sleep(2)

app.connect(title="Media Player")
time.sleep(2)
music_app = app.MediaPlayer

if not music_app.is_maximized():
    music_app.maximize()

recent_plays_tab = music_app.Instrumental.click_input()
time.sleep(12)

openfile_tab = music_app.Openfile.click_input()
time.sleep(2)

select_tab = music_app.Flute.click_input()
keyboard.send_keys('{TAB 4}')
time.sleep(2)
keyboard.send_keys('{ENTER}')
time.sleep(15)

music_app.Back.click_input()
time.sleep(3)

music_lib = music_app.Musiclibrary.click_input()
time.sleep(3)
music_app.Addfolder.click_input()
time.sleep(3)
music_app.Soundrecordings.click_input()
keyboard.send_keys('{TAB 3}')
time.sleep(2)
keyboard.send_keys('{ENTER}')
time.sleep(3)

music_app.Albums.click_input()
music_app.UnknownalbumVoiceRecorder.click_input()
music_app.Airtel.click_input()
music_app.Play.click_input()
time.sleep(30)

# music_app.Airtel.Play.click_input()
# time.sleep(2)
#
# albums_tab = music_app.Albums.click_input()
# time.sleep(3)
#
# music_app.UnknownalbumVoiceRecoder.click_input()
#
# music_app.Back.click_input()








