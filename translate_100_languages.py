from random import sample
from googletrans import Translator,LANGUAGES
import speech_recognition as sr


r = sr.Recognizer()
mic = sr.Microphone()

print ("Te escucho")
with mic as source: 
   r.pause_threshold = 1 
   r.adjust_for_ambient_noise(source) 
   audio = r.listen(source) 
result = r.recognize_google(audio)

for language in LANGUAGES:
   t = Translator().translate(result, dest = language)
   
   print (LANGUAGES [language] + ': ' + t.text)
