import os
import eel
from engine.features import * 
from engine.command import * 

eel.init("www")

playAssistantSound()

from engine.features import signupUser
res = signupUser()

@eel.expose
def init():
    eel.hideStart(res)
    
os.system('start chrome.exe --app="http://localhost:8000/index.html"')
eel.start('index.html', mode=None, host='localhost', block=True)