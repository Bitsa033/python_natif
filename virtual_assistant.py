import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak out the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        # recognizer.adjust_for_ambient_noise(source)
        # audio = recognizer.listen(source)
        try:
            print("Je vous écoute...")
            # query = recognizer.recognize_google(audio)
            query=input('entrer votre message: ')
            print("Message:", query)
            return query
        except Exception as e:
            print("S'il vous plait, Je ne vous écoute pas. Pouvez-vous repété ?")
            return ""

# Main function for the virtual assistant
def main():
    speak("Bonjour ! Je suis votre assistant virtuel. Comment puis-je vous aidé?")
    while True:
        query = listen().lower()

        if "bonjour comment vas-tu?" in query:
            speak("Bonjour,je vais bien et toi?")
        elif "ton nom" in query:
            speak("Je m'appelle alicia.")
        elif "je te pose une question" in query:
            speak("oui je t'écoute!")
        elif "ta couleur" in query:
            speak("J'aime la couleur rouge.")
        elif "pourquoi" in query:
            speak("parce qu'elle représente l'amour.")
            speak("et toi quelle est ta couleur préférée?")
        elif "moi j'aime la couleur bleu" in query:
            speak("ouaa! c'est génial, une couleur divine en effet")
        elif "joue moi une musique" in query:
            speak("je ne peux pas car je n'ai pas assez de connexion internet.")
        elif "combien font 1+2" in query:
            speak("1+2 font")
            speak(1+2)
        elif "au revoir" in query or "bye" in query:
            speak("Au revoir et Merci!")
            break
        else:
            speak("Désolé, Je vous écoute à peine. Pouvez-vous repété ?")

if __name__ == "__main__":
    main()
