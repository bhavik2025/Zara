import pyttsx3
import speech_recognition as sr
import eel
import time
import pyautogui as autogui

eel.init('www') 

@eel.expose
def speak(text):
    text = str(text)
    if len(text) > 250:
        speed = 180
    else:
        speed = 130
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',speed) 
    eel.DisplayMessage(text)  # Ensure this function exists on the frontend
    engine.say(text)
    eel.receiverText(text)    # Ensure this function exists on the frontend
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        eel.DisplayMessage("listening......")  # Ensure this function exists on the frontend
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)
    
    try:
        eel.DisplayMessage("recognizing......")
        query = r.recognize_google(audio, language='en-in')
        eel.DisplayMessage(query)
        time.sleep(2)
    except Exception as e:
        return ""
    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        if not query:
            eel.DisplayMessage("Sorry, I didn't catch that. Please try again.")
            speak("Sorry, I didn't catch that. Please try again.")
            return
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    
    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif 'on youtube' in query or 'in youtube' in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        # elif 'on google' in query or 'in google' in query:
        #     from engine.features import PlayYoutube
        #     PlayYoutube(query)
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            contact_no, name = findContact(query)
            if contact_no != 0:
                if "send message" in query: 
                    message = 'message'
                    speak("what message to send")
                    query = takecommand()
                elif "phone call" in query:
                    message = 'call'
                else:
                    message = 'video call'                                    
                whatsApp(contact_no, query, message, name)
        elif "your name" in query:
            try:
                from engine.features import zara
                zara()
            except Exception as e:
                print(f"Error Occure : {e}")
        elif "store this" in query:
            speak("what information to store...")
            query = takecommand()
            from engine.features import memory
            result = memory(query)
            if result == True:
                speak("Data Stored...")
            else:
                speak(result)
        elif "close yourself" in query or "terminate yourself" in query:
            if "close" in query:
                speak("Closing myself, feel free to reach out again...")
            else:
                speak("terminating myself, feel free to reach out again...")
            autogui.keyDown("alt")
            autogui.press("f4")
            time.sleep(2)
            autogui.keyUp("alt")
        else:
            try:
                from engine.features import chatBot  
                chatBot(query)
            except Exception as e:
                print(f"Error is : {e}")

    except Exception as e:
        print(f"Error: {e}")
    eel.ShowHood()  # Ensure this function exists on the frontend