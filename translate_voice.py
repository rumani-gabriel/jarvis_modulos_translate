from googletrans import Translator
import pyttsx3
import speech_recognition as sr

#se ejecuta este for en el caso de querer ver los datos de la configuración de voz del sistema

# voices = engine.getProperty('voices') 
# for voice in voices: 
#   print("Voice:") 
#   print(" - ID: %s" % voice.id) 
#   print(" - Name: %s" % voice.name) 
#   print(" - Languages: %s" % voice.languages) 
#   print(" - Gender: %s" % voice.gender) 
#   print(" - Age: %s" % voice.age)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
engine.setProperty('rate', 130)

#inicializamos el reconedor de voz
r = sr.Recognizer()

#con el siguiente script encuentro el dispositivo de entrada que quiero utilizar
# print(sr.Microphone.list_microphone_names())

mic = sr.Microphone()

with mic as source: 
   r.pause_threshold = 1 
   r.adjust_for_ambient_noise(source) 
   audio = r.listen(source) 
result = r.recognize_google(audio)


p = Translator()
k = p.translate(result, dest='en')
translated = str(k.text)


print(translated)


#tiempo de latencia 3 seg
engine.say(translated)
engine.runAndWait()
