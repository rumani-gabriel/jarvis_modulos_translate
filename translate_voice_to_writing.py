
from googletrans import Translator,LANGUAGES
import speech_recognition as sr

translator= Translator()
r = sr.Recognizer()
mic = sr.Microphone()

print ("Te escucho")
with mic as source: 
   r.pause_threshold = 1 
   r.adjust_for_ambient_noise(source) 
   audio = r.listen(source) 
result = r.recognize_google(audio)


print (result)

dt= translator.detect(result)

print(dt.lang)
# print (LANGUAGES)

translate= translator.translate (result, dest="es")

print (translate.text)



