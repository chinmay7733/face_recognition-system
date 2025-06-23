import face_recognition
import cv2
import numpy as np
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import requests
import json
from keyboard import press
from keyboard import press_and_release


# for chrome
chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
web = webbrowser.get('chrome')


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def checkpasswrd():
    su = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        su.pause_threshold = 1
        audio = su.listen(source)

    try:
        print("Recognizing...")
        passwrd = su.recognize_google(audio, language='en-in')
        print(f"User said: {passwrd}\n")

    except Exception:

        print("Say that again please...")
        return "None"
    return passwrd

def takeCommand():
    # It takes microphone input from the user and returns string output

    su = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        su.pause_threshold = 1
        audio = su.listen(source)

    try:
        print("Recognizing...")
        querry = su.recognize_google(audio, language='en-in')
        print(f"User said: {querry}\n")

    except Exception:

        print("Say that again please...")
        return "None"
    return querry

def wishMe(m):
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak(f"Good Morning!{m} sir")
    elif 12 <= hour < 18:
        speak(f"Good Afternoon!{m} sir")
    else:
        speak(f"Good Evening!{m} sir")

    speak("I am Jarvis Sir. Please tell me how may I help you")


# Face recognition or face password
vidio_capture = cv2.VideoCapture(0)

# Load known faces
CHINMAY_image = face_recognition.load_image_file("faces/image.png")
CHINMAY_encoding = face_recognition.face_encodings(CHINMAY_image)[0]

known_face_encodings = [CHINMAY_encoding]
known_face_names = ["CHINMAY"]

# list of expected students
students = known_face_names.copy()

face_locations = []

face_encodings = []

i = 0
n = []
while True:
    _, frame = vidio_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#     recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            n.append(name)
            # Add the text if a person present
            if name in known_face_names:
                font = cv2.FONT_HERSHEY_COMPLEX_SMALL
                bottomLeftCornerOfText = (5, 25)
                fontScale = 1
                fontColor = (25, 0, 0)
                thickness = 2
                lineType = 1
                cv2.putText(frame, " Welcome sir! Press 'q' for next actions ", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
        else:
            speak("face doesn't match")
            i += 1
    cv2.imshow("Jarvis", frame)
    if cv2.waitKey(1) & 0xFF == ord("q") or i == 3:
        break
vidio_capture.release()
cv2.destroyAllWindows()


if i < 5:
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            web.open("youtube.com")
            while True:
                query = takeCommand().lower()
                if 'mute vidio' in query:
                    press('m')

                elif 'pause vidio' or 'start vidio' in query:
                    press('k')

                elif 'next' in query:
                    press('l')

                elif 'go back' in query:
                    press('j')

                elif 'search' in query:
                    press('/')
                    speak('what would you like to search')
                    sh = takeCommand().lower()
                    press_and_release(sh)

                elif 'open caption' in query:
                    press('c')

                elif 'speed up' in query:
                    press_and_release('shift + .')

                elif 'speed down' in query:
                    press_and_release('shift + ,')

                elif 'started vidio to beginning' in query:
                    press('0')

                elif 'Move to the next video ' in query:
                    press_and_release('shift + n')

                elif 'Move to the previous video ' in query:
                    press_and_release('shift + p')



        elif 'open emoji' in query:
            press_and_release('win + .')

        elif 'open google' in query:
            web.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'today date' in query:
            strTime = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"sir, today date is {strTime}")

        elif 'lock my pc ' in query:
            press_and_release('Wind + l')

        elif 'display desktop' in query:
            press_and_release('Win + d')

        elif 'next' in query:
            press_and_release('alt + esc')

        elif 'open Task view' in query:
            pass

        elif 'take screen shot' in query:
            press_and_release('win + shift + s')

        elif 'take screen shot' in query:
            press_and_release('win + shift + s')

        elif 'open terminal' in query:
            press_and_release('win + x + i')

        elif 'about system' in query:
            press_and_release('win + x + y')

        elif 'open device manager' in query:
            press_and_release('win + x + k')

        elif 'open networks' in query:
            press_and_release('win + x + w')

        elif 'open device manager' in query:
            press_and_release('win + x + m')

        elif 'open computer management' in query:
            press_and_release('win + x + g')

        elif 'open task manager' in query:
            press_and_release('win + x + t')

        elif 'open settings' in query:
            press_and_release('win + x + n')

        elif 'open files' in query:
            press_and_release('win + x + e')

        elif 'open search' in query:
            press_and_release('win + x + s')
            speak('what would we like to search')

        elif 'open run' in query:
            press_and_release('win + r')

        elif 'shutdown computer' in query:
            press_and_release('win + u + u')

        elif 'restart computer' in query:
            press_and_release('win + u + r')

        elif 'open ms word' in query:
            press_and_release('')


        elif'open chrome' in query:
            while True:
                query = str(takeCommand().lower())
                if 'open new tab' in query:
                    press_and_release('ctrl + t')

                elif 'close tab' in query:
                    press_and_release('ctrl + w')

                elif 'open new window' in query:
                    press_and_release('ctrl + n')

                elif 'open history' in query:
                    press_and_release('ctrl + h')

                elif 'open download' in query:
                    press_and_release('ctrl + j')

                elif 'open bookmark' in query:
                    press_and_release('ctrl + d')
                    press('enter')

                elif 'open incognito' in query:
                    press_and_release('ctrl + shift + n')

                elif 'switch tab' in query:
                    tab = query.replace('switch tab', '')
                    Tab = tab.replace('to', '')
                    num = Tab
                    press_and_release(f'ctrl + {num}')

                elif 'open' in query:
                    name = query.replace('open', '')
                    Name = str(name)
                    string = Name + '.com'
                    string_2 = string.replace(' ', '')
                    web.open(string_2)

        elif 'close the program' in query:
            speak('thankyou for coming')
            break

        elif 'about news' in query:
            speak("What type of news are you interested in? ")
            query = takeCommand().lower()
            url = f"https://newsapi.org/v2/everything?q={query}&apiKey=bac8de593f2747b296d8d78633cf5037"
            r = requests.get(url)
            news = json.loads(r.text)
            # print(news, type(news))
            for article in news["articles"]:
                for i in range(5):
                    print(article["title"])
                    print(article["description"])
                    print("--------------------------------------")
                break