from shlex import quote
import subprocess
from playsound import playsound
import eel
import os
import pyautogui
from engine.command import *
from engine.config import *
import pywhatkit as kit
import sqlite3
import webbrowser
import pyaudio            
import pvporcupine
import struct
import time
from engine.helper import extract_yt_term, remove_words
from hugchat import hugchat
import speech_recognition as sr

conn = sqlite3.connect("zara.db")
cursor = conn.cursor()

eel.init('www') 

# Playing assiteant sound Finction

@eel.expose
def playAssistantSound():
    music_dir = "www/assets/audio/start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("hello", "")
    query = query.replace("open", "")
    query.lower()
    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")
    
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def hotword():
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as sourse:
                print("Listening...")
                audio = r.listen(sourse, timeout=2)
            word = r.recognize_google(audio)
            print(word)
            if (word.lower() == "zara"):
                import pyautogui as autogui
                autogui.keyDown("alt")
                autogui.press("z")
                time.sleep(2)
                autogui.keyUp("alt")
        except Exception as e:
            print(e)

# find contacts
def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str
 
        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    
def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12
        zara_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        zara_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        zara_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(zara_message)

# chat bot 
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine/cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    speak(response)
    print(response)
    return response

# asking name 
def zara():
    speak("My Name is ZARA, How can i Assiste you today.")

# store data in memory
def memory(query):
    try:
        if query == "":
            speak("What Information To Store...")
            TackAgain = takecommand()
            memory(TackAgain)
            return False
        else:
            cursor.execute("INSERT INTO memory (id, 'info') VALUES (null, ?)", (query,))
            conn.commit()
            return True
    except Exception as e:
        return e
    
# input data
@eel.expose
def insertSys(keyword,path):
    try:
        cursor.execute("INSERT INTO sys_command (id, 'name', 'path') VALUES (null, ?, ?)", (keyword,path))
        conn.commit()
        speak("Data Added...")
    except Exception as e:
        speak(e)

@eel.expose
def insertWeb(keyword,path):
    try:
        cursor.execute("INSERT INTO web_command (id, 'name', 'url') VALUES (null, ?, ?)", (keyword,path))
        conn.commit()
        speak("Data Added...")
    except Exception as e:
        speak(e)

@eel.expose
def insertConatct(name,no):
    try:
        cursor.execute("INSERT INTO contacts (id, 'name', 'mobile_no', 'email') VALUES (null, ?, ?, null)", (name,no))
        conn.commit()
        speak("Data Added...")
    except Exception as e:
        speak(e)

# Display data

@eel.expose
def displayPersonalDetails():
    cursor.execute("SELECT * FROM personal_details")
    results = cursor.fetchall()
    return results

@eel.expose
def displaySysCommand():
    cursor.execute("SELECT * FROM sys_command")
    results = cursor.fetchall()
    return results

@eel.expose
def displayWebCommand():
    cursor.execute("SELECT * FROM web_command")
    results = cursor.fetchall()
    return results

@eel.expose
def displayContact():
    cursor.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    return results

@eel.expose
def displayMemory():
    cursor.execute("SELECT * FROM memory")
    results = cursor.fetchall()
    return results

# Delete Data

@eel.expose
def deleteSystem(id):
    try:
        cursor.execute("DELETE FROM sys_command WHERE id = ?", (id))
        conn.commit()   
        speak("Data Deleted...")
    except Exception as e:
        speak(e)

@eel.expose
def deleteWeb(id):
    try:
        cursor.execute("DELETE FROM web_command WHERE id = ?", (id))
        conn.commit()   
        speak("Data Deleted...")
    except Exception as e:
        speak(e)

@eel.expose
def deleteContact(id):
    try:
        cursor.execute("DELETE FROM contacts WHERE id = ?", (id))
        conn.commit()   
        speak("Contact Deleted...")
    except Exception as e:
        speak(e)

@eel.expose
def deleteMemory(id):
    try:
        cursor.execute("DELETE FROM memory WHERE id = ?", (id))
        conn.commit()   
        speak("Memory Deleted...")
    except Exception as e:
        speak(e)

def signupUser():
    try:
        cursor.execute("SELECT * FROM personal_details")
        chk = cursor.fetchall()
        if chk:
            return 1
        else:   
            return 0
    except Exception as e:
        print(f"Error in signupUser: {e}")
        return 0

@eel.expose
def userinsert(n,p,m,mo):
    try:
        cursor.execute("INSERT INTO personal_details (id, 'name','email', 'password','mo') VALUES (null, ?,?,?,?)",(n,m,p,mo))
        conn.commit()
        speak("Ragistration Done...")
    except Exception as e:
        speak("something is wrong to DataBase...")


@eel.expose
def updatePD(n,p,m,mo):
    try:
        cursor.execute("UPDATE personal_details SET name=?, email=?, password=?, mo=? WHERE id = 1",(n,m,p,mo))
        conn.commit()
        speak("Profile Updated...")
    except Exception as e:
        speak("something is wrong to DataBase...")
    
@eel.expose
def DeletePD():
    try:
        cursor.execute("delete from personal_details")
        conn.commit()
        speak("Profile Deleted...")
        speak("Visit Again, Have A good Day...")
        pyautogui.keyDown("alt")
        pyautogui.press("f4")
        pyautogui.keyUp("alt")
    except Exception as e:
        speak("something is wrong to DataBase...")

@eel.expose
def checkUser(m,p):
    try:
        cursor.execute("SELECT * FROM personal_details WHERE email = ? and password = ? ",(m,p))
        res = cursor.fetchall()
        if res:
            speak("Hello, Wellcome, How Can I Help You...")
            return 1
        else:
            return 0
    except Exception as e:
        speak("something is wrong to DataBase...")