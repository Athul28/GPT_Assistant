#python text-to-speech module
import pyttsx3

#module to take voice inputs
import speech_recognition as sr

#other modules
import datetime
import wikipedia
import webbrowser

#module used to provide interaction between the user and the operating system
import os

#ChatGpt API
import openai
openai.api_key = "Enter Your API KEY"


#Setting up the voice for text to speech module
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#Function to get answers form chatgpt
def chatgpt(prompt):
    try:
        model_engine = "text-davinci-003"
        completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        )
        # Print the response
        response=completion.choices[0].text
        print(response)
        speak(response)
    except Exception as e:
        speak("Sorry, accessing chat GPT isn't possible right now")
        speak("Ask me anything else")



#Function to wish the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am GPT Assistant. Please tell me how may I help you")       


#Function to take inputs form the user as voice
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        # print(e)    
        print("Say that again please...\n")  
        return "none_"
    
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
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
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://google.com/")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")   

        elif 'play music' in query:
            music_dir = "C:\\Users\\Admin\\Desktop\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'your name' in query:
            speak("My name is GPT Assistant")

        elif 'exit' in query:
            speak("Ok sir")
            exit()
            
        elif 'none_' in query:
            continue
        
        elif 'your creator' in query:
            speak("Athul Bhandary created me")

        else:
                chatgpt(query)
