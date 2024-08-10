import datetime
import os
import smtplib
import sys
import winsound
import pywikihow
import requests
import time
import webbrowser
import cv2
import pyautogui
import pyjokes
from pywikihow import search_wikihow
import pyttsx3
import pywhatkit as kit
import speech_recognition as sr
import wikipedia
import psutil
from requests import get
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Text to speech function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Function to greet the user based on the time of day and announce the current time
def wish():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    if hour >= 0 and hour < 12:
        speak(f"Good morning sir! The time is {hour}:{minute:02d} AM.")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon sir! The time is {hour % 12 or 12}:{minute:02d} PM.")
    else:
        speak(f"Good evening sir! The time is {hour % 12 or 12}:{minute:02d} PM.")
    speak("I am your Jarvis sir. How can I help you today?")

# Function to capture the user's voice input with error handling
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("Listening timed out, please try again.")
            return "none"
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that. Please say that again.")
            return "none"
        except sr.RequestError:
            speak("Sorry, I am unable to process your request right now. Please check your network connection.")
            return "none"
        return query.lower()

# Function to send email
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your_email@example.com', 'password')  # Use your actual credentials
        server.sendmail('your_email@example.com', to, content)
        server.close()
        speak("Email has been sent.")
    except Exception as e:
        speak("Sorry sir, I am not able to send this email.")
        print(e)

# Function to send email with attachment
def sendEmailWithAttachment(to, subject, message, file_location):
    try:
        email = 'your_email@example.com'  # Use your actual email
        password = 'your_password'  # Use your actual password

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        # Setup the attachment
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={filename}")

        # Attach the attachment to the MIMEMultipart object
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, to, text)
        server.quit()
        speak("Email has been sent with the attachment.")
    except Exception as e:
        speak("Sorry sir, I am not able to send this email.")
        print(e)

# Function to fetch and read news
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=f71c7c1bfe4f4262befa5e6b059d9edf'
    try:
        main_page = requests.get(main_url).json()
        articles = main_page["articles"]
        head = []
        day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
        for ar in articles:
            head.append(ar["title"])
        for i in range(min(len(day), len(head))):  # Ensure you don't go out of bounds
            speak(f"Today's {day[i]} news is: {head[i]}")
    except Exception as e:
        speak("Sorry, I couldn't fetch the news. Please try again later.")
        print(e)

# Function to set alarm
def alarm(Timing):
    try:
        altime = datetime.datetime.strptime(Timing, "%I:%M %p")
        while True:
            now = datetime.datetime.now()
            if now.hour == altime.hour and now.minute == altime.minute:
                speak("It's time to wake up!")
                winsound.Beep(1000, 1000)  # Frequency and duration
                break
            time.sleep(30)
    except ValueError as e:
        speak("I could not understand the time format. Please use HH:MM AM/PM format.")
        print(e)

def TaskExecution():
    wish()
    while True:
        query = takecommand()

        # Logic building for tasks
        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            speak("Okay sir, closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            speak("Okay sir, closing Command Prompt")
            os.system("taskkill /f /im cmd.exe")

        elif "open file explorer" in query:
            os.system("explorer")

        elif "close file explorer" in query:
            speak("Okay sir, closing File Explorer")
            os.system("taskkill /f /im explorer.exe")

        elif "open calculator" in query:
            os.system("calc")

        elif "close calculator" in query:
            speak("Okay sir, closing Calculator")
            os.system("taskkill /f /im calculator.exe")

        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "volume mute" in query or "mute" in query:
            pyautogui.press("volumemute")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                speak("Unable to access the camera")
                print("Unable to access the camera")
                continue

            while True:
                ret, img = cap.read()
                if not ret:
                    speak("Failed to grab frame")
                    print("Failed to grab frame")
                    break
                cv2.imshow('webcam', img)

                if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\User\\Music"
            songs = os.listdir(music_dir)
            if songs:  # Check if there are any songs in the directory
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))
                        break
            else:
                speak("No music found in the directory")

        elif "ip address" in query:
            try:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")
            except Exception as e:
                speak("Unable to get the IP address")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
                print(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("The search term is too ambiguous. Please be more specific.")
            except Exception as e:
                speak("Could not find information on Wikipedia")

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        elif "open stackoverflow" in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif "open google" in query:
            speak("Sir, what should I search on Google?")
            cm = takecommand()
            webbrowser.open(f"https://www.google.com/search?q={cm}")

        elif "send message" in query:
            try:
                kit.sendwhatmsg("+919999999999", "This is a testing protocol", 15, 30)  # Use a valid number
            except Exception as e:
                speak("Failed to send the message")

        elif "play songs on youtube" in query:
            kit.playonyt("not afraid")

        elif "email to leo" in query:
            try:
                speak("What should I say?")
                query = takecommand()
                if "send a file" in query:
                    to = 'leo@example.com'  # Placeholder email
                    speak("Okay sir, what is the subject for this email?")
                    subject = takecommand()
                    speak("And sir, what is the message for this email?")
                    message = takecommand()
                    speak("Sir, please enter the correct path of the file into the shell")
                    file_location = input("Please enter the path here: ")

                    speak("Please wait, I am sending the email now.")
                    sendEmailWithAttachment(to, subject, message, file_location)
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email to Leo")

        elif "set alarm" in query:
            speak("Please tell me the time to set the alarm in HH:MM AM/PM format.")
            alarm_time = takecommand()
            speak(f"Setting an alarm for {alarm_time}.")
            alarm(alarm_time)

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            speak("Putting the system to sleep")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("Please wait sir, fetching the latest news")
            news()

        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day.")
            sys.exit()

        elif "where am I" in query or "where we are" in query:
            speak("Wait sir, let me check")
            try:
                ipADD = requests.get('https://api.ipify.org').text
                print(ipADD)
                url = f'https://get.geojs.io/v1/ip/geo/{ipADD}.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()

                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir, I am not sure, but I think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry sir, due to network issues I am not able to find where we are")

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("Sir, please tell me the name for this screenshot file")
            name = takecommand()
            speak("Please sir hold the screen for few seconds, I am taking a screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir, the screenshot is saved in our main folder. Now I am ready for your next command.")

        elif "hello" in query or "hey" in query:
            speak("Hello sir, may I help you with something?")

        elif "how are you" in query:
            speak("I am fine sir, what about you?")

        elif "I am also good" in query or "I am fine" in query:
            speak("That's great to hear from you")

        elif "thank you" in query or "thanks" in query:
            speak("It's my pleasure sir")

        elif "you can sleep" in query or "sleep now" in query:
            speak("Okay sir, I am going to sleep. You can call me anytime.")
            break


        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            if percentage >= 75:
                speak("we have enough power to continue our work")
            elif 40 <= percentage < 75:
                speak("we should connect our system to charging point to charge our battery")
            elif 15 <= percentage < 40:
                speak("we don't have enough power to work, please connect to charging")
            elif percentage < 15:
                speak("we have very low power, please connect to charging the system will shutdown very soon")

        elif "activate how to do mode" in query:
            speak("how to do mode is activated")
            while True:
                speak("please tell me what you want to know")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir, how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, I am not able to find this")

        elif "internet speed" in query:
            try:
                os.system('cmd /k "speedtest"')
            except:
                speak("there is no internet connection")

        speak("Sir, do you have any other work?")

if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission:
            TaskExecution()
        elif "goodbye" in permission:
            speak("Thanks for using me sir, have a good day.")
            sys.exit()
