import speech_recognition as sr
import pyttsx3
import webbrowser

def menu_assistant():
    while True:
        speak("Bienvenue dans le programme d'assistance virtuelle")
        speak("Tapez 1 pour lire des vidéos")
        speak("Tapez 2 pour quitter")
        ecouter=int(listen())
        if ecouter==1:
            speak("Programme d'assistance de lecture des vidéos")
            ecouter_la_musique()
        elif ecouter==2:
            speak("Fermeture du programme encours..")
            break
        else:
            speak("Commande invalide, veuillez recommencer")
# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        # recognizer.adjust_for_ambient_noise(source)
        try:
            print("Je vous écoute...")
            # audio = recognizer.listen(source)
            # query = recognizer.recognize_google(audio,language='fr-FR')
            query=input('entrer votre message: ')
            print("Message:", query)
            return query
                
        except:
            print("Je ne vous écoute pas, parlez à haute voix!")
            return ""
        
# Initialize the speech recognizer and text-to-speech engine
# recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak out the response
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def open_youtube(link):
    webbrowser.open(link)
    
def ecouter_la_musique():
    while True:
        query = listen().lower()

        if "lance la musique de" in query:
            chanteur=query.replace('lance la musique de',"")
            print(chanteur)
            message="ouveture du navigateur et lancement de la musique de "+chanteur
            speak(message)
            link="https://www.youtube.com/results?search_query="+chanteur.lstrip()
            print(link)
            open_youtube(link)
        
        elif "au revoir" in query or "bye" in query:
            speak("Au revoir et Merci!")
            break
        else:
            speak("Désolé, Je vous écoute à peine.Parlez à haute voix!")
