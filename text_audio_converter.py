import speech_recognition as sr
from gtts import gTTS
import os

def text_to_speech(text, language='fr'):
    """Convertit du texte en fichier audio"""
    try:
        # Création de l'objet gTTS
        tts = gTTS(text=text, lang=language)
        
        # Sauvegarde le fichier audio
        tts.save("output.mp3")
    
        print("Audio généré avec succès!")
        
    except Exception as e:
        print(f"Une erreur s'est produite: {str(e)}")

def speech_to_text():
    """Convertit l'audio en texte"""
    # Création du recognizer
    recognizer = sr.Recognizer()
    
    try:
        # Utilisation du microphone
        with sr.Microphone() as source:
            print("Parlez maintenant...")
            # Écoute l'audio du microphone
            audio = recognizer.listen(source)
            print("Traitement de l'audio...")
            
            # Conversion en texte
            text = recognizer.recognize_google(audio, language='fr-FR')
            print(f"Texte reconnu: {text}")
            return text
            
    except sr.UnknownValueError:
        print("Désolé, je n'ai pas compris l'audio")
    except sr.RequestError as e:
        print(f"Erreur lors de la requête au service de reconnaissance vocale: {str(e)}")

def main():
    while True:
        print("\n1. Convertir du texte en audio")
        print("2. Convertir de l'audio en texte")
        print("3. Quitter")
        
        choix = input("Choisissez une option (1-3): ")
        
        if choix == '1':
            texte = input("Entrez le texte à convertir: ")
            text_to_speech(texte)
        elif choix == '2':
            speech_to_text()
        elif choix == '3':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main() 