import pyttsx3
# install pyaudio
# install espeak
engine = pyttsx3.init()
engine.setProperty('engine', 'flite')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)
engine.say("The current weather in Malta is 42 degree centigrade")
engine.runAndWait()
